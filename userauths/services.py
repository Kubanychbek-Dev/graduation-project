from django.conf import settings
from django.core.mail import send_mail


def send_register_email(email):
    send_mail(
        subject="Привет, добро пожаловать на платформу ESHOP",
        message="Вы успешно зарегистрировались",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email, ]
    )


def send_gratitude_text(email, amount):
    send_mail(
        subject="Благодарим вас за покупку в ESHOP",
        message=f"ESHOP\n\nСумма вашего заказа: {amount}, ждем вас снова",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email, ]
    )
