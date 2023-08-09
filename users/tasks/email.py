from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_activation_code_email_task(subject: str, message: str, email: str):
    send_mail(
        subject=subject,
        message=message,
        from_email="suslanchikmopl@gmail.com",
        recipient_list=[email]
    )
