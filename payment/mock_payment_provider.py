import uuid
from .payment_providers import PaymentProvider


class MockPaymentProvider(PaymentProvider):
  def process_payment(self, order, amount, token):
    print("Payment processing")
    print(order)
    print(amount)

    if token:
      transaction_id = str(uuid.uuid4())
      return True, transaction_id
  
  def refund_payment(self, order, amount):
    print("Mock refund")
    return True
