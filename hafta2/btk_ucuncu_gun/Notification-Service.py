from dataclasses import dataclass
from typing import Protocol

# ==========================================
# 1. VERİ MODELİ (DTO - Data Transfer Object)
# ==========================================
@dataclass
class Message:
    """
    Sistem içindeki mesaj verilerini taşıyan veri yapısıdır.
    İş mantığı barındırmaz, sadece alıcı ve içerik bilgisini tutar.
    """
    to: str      # Mesajın kime gideceği
    content: str # Mesajın içeriği

# ==========================================
# 2. SOYUTLAMA / ARAYÜZ (INTERFACE)
# ==========================================
class Sender(Protocol):
    """
    Tüm gönderici sınıflarının uyması gereken sözleşmedir (Interface).
    Bu protokolü kullanan her sınıf, 'send' metodunu içermek zorundadır.
    Bu sayede sistem, arka planda hangi sınıfın çalıştığını bilmeden işlem yapabilir.
    """
    def send(self, msg: str) -> None: 
        ... 

# ==========================================
# 3. SOMUT STRATEJİLER (CONCRETE STRATEGIES)
# ==========================================
class EmailSender:
    """
    Sender protokolünü uygulayan (implement eden) Email sınıfı.
    Email gönderme işlemlerine ait spesifik kodlar burada yer alır.
    """
    def send(self, msg: str) -> None:
        print(f"[Email Modülü] Email gönderildi: {msg}")

class SMSSender:
    """
    Sender protokolünü uygulayan SMS sınıfı.
    SMS API entegrasyonları ve ilgili mantık burada yer alır.
    """
    def send(self, msg: str) -> None:
        print(f"[SMS Modülü] SMS gönderildi: {msg}")

# ==========================================
# 4. BAĞLAM / YÖNETİCİ (CONTEXT)
# ==========================================
class Notifier:
    """
    Bildirim sürecini yöneten ana sınıftır.
    Hangi bildirim türünün (SMS, Email) kullanılacağına karar vermez;
    sadece kendisine verilen 'Sender' nesnesini çalıştırır.
    """
    def __init__(self, sender: Sender):
        # Dependency Injection: Gönderici sınıfı dışarıdan enjekte edilir.
        # Bu sayede Notifier sınıfı, EmailSender veya SMSSender'a bağımlı kalmaz.
        self.sender = sender 

    def notify(self, message: Message) -> None:
        # Gelen mesaj verisi formatlanır.
        formatted_msg = f"Kime: {message.to} -> İçerik: {message.content}"
        
        # Polymorphism: self.sender'ın ne olduğu (Email mi SMS mi) bilinmez.
        # Sadece .send() yeteneği olduğu bilinir ve tetiklenir.
        self.sender.send(formatted_msg)

# ==========================================
# 5. TEST / KULLANIM (CLIENT CODE)
# ==========================================

# Notifier sınıfı başlatılıyor ve 'EmailSender' stratejisi enjekte ediliyor.
# Artık bu notifier örneği, verilen her emri Email olarak işleyecek.
notifier = Notifier(EmailSender())

# Message nesnesi (Kime, İçerik) oluşturuluyor ve işlenmesi için gönderiliyor.
# Beklenen Çıktı: [Email Modülü] Email gönderildi: ...
notifier.notify(Message("Ali", "Eve geç kalma"))


# Notifier sınıfı tekrar başlatılıyor ama bu sefer 'SMSSender' stratejisi veriliyor.
# Kodun geri kalanı değişmese bile davranış (behavior) değişmiş oluyor.
notifier_ = Notifier(SMSSender())

# Beklenen Çıktı: [SMS Modülü] SMS gönderildi: ...
notifier_.notify(Message("Ayşe", "Okula git."))