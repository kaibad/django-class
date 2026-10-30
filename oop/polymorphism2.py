class Payment:
    def process_payment(self,amount):
        print("Processing Payment ...")

class CreditCardPayment(Payment):
    def process_payment(self,amount):
        print(f"Processing Credit Card Payment of ${amount} ... ")

class PayPalPayment(Payment):
    def process_payment(self,amount):
        print(f"Processing PayPal Payment of ${amount} ... ")

class BankTransferPayment(Payment):
    def process_payment(self,amount):
        print(f"Processing Bank Transfer Payment of ${amount} ... ")  

payment1 = CreditCardPayment()
payment2 = PayPalPayment()
payment3 = BankTransferPayment()

# polymorphism allows us to use the same method name for different types of objects, and the appropriate method will be called based on the object that is being used.
payments = [payment1, payment2, payment3]

for payment in payments:
    payment.process_payment(100)
