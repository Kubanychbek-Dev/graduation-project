class PaymentProvider:
  def process_payment(self, order, amount, token):
    raise NotImplementedError
  
  def refund_payment(self, order, amount):
    raise NotImplementedError
  