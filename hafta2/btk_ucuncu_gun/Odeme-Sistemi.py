'''   
class PricingStrategy:
    def calculate_price(self, base_price):
        pass


class NormalPricing(PricingStrategy):
    def calculate_price(self, base_price):
        return base_price
   

class StudentPricing(PricingStrategy):
    def calculate_price(self, base_price):
  

class BlackFridayPricing(PricingStrategy):
    def calculate_price(self, base_price):
        return base_price * 0.70
    


class PaymentMethod:
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"{amount} TL kredi kartı ile ödendi."
    
class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        return f"{amount} TL PayPal ile ödendi."
    

class Logger:
    __instance = None

    def __new__ (cls):
        if cls.instance is None:
            cls.instance = super (Logger, cls).__new__(cls)
        return cls.instance
    def log(self):
        return f"Log kaydı oluşturuldu.{self}"
    
    
class PaymentFactory:
    @staticmethod
    def create(payment:str)->PaymentMethod:
        if payment == "credit_card":
            return CreditCardPayment()
        elif payment == "paypal":
            return PayPalPayment()
        else:
            raise ValueError("Geçersiz ödeme yöntemi.")
    

price = PricingStrategy().base_price 
payment_method = PaymentFactory.create(Payment_Method())
final_price = StudentPricing().calculate_price(price)

'''

class Logger:
    instance = None

    def __new__ (cls):
        if cls.instance is None:
            cls.instance = super (Logger, cls).__new__(cls)
        return cls.instance
    def log(self , msg:str):
        print("[LOG]",msg)
    
class PricingStrategy:
    def calculate(self, base:float)-> float:...
    
class NoDiscount(PricingStrategy):
    def calculate(self, base:float)-> float:
        return base
    
class StudentDiscount(PricingStrategy):
    def calculate(self, base:float)-> float:
        return base * 0.90
    
class BlackFridayDiscount(PricingStrategy):
    def calculate(self, base:float)-> float:
        return base * 0.70
    
class PaymentMethod:
    def pay(self, amount:float): ...

class CreditCardPayment(PaymentMethod):
    def pay(self, amount:float):
        return print(f"{amount} TL kredi kartı ile ödendi.")
    
class PayPalPayment(PaymentMethod):
    def pay(self, amount:float):
        return print(f"{amount} TL PayPal ile ödendi.")
    

class PaymentFactory:
    @staticmethod
    def create(payment:str)->PaymentMethod:
        if payment == "credit_card":
            return CreditCardPayment()
        
        if payment == "paypal":
            return PayPalPayment()
        
        raise ValueError("Geçersiz ödeme yöntemi.") 
    
def process_payment(base_price:float, strategy:PricingStrategy, payment_method:str):

    log = Logger()

    final_price = strategy.calculate(base_price)
    log.log(f"{final_price} TL ödeme işlendi.")

    payment = PaymentFactory.create(payment_method)

    payment.pay(final_price)
    log.log(f"Ödeme {payment_method} ile tamamlandı.")


process_payment(100.0, StudentDiscount(), "credit_card")


        
        

