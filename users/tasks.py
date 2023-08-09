from datetime import datetime

from celery import shared_task
from django.core.cache import cache
from django.core.mail import send_mail


@shared_task()
def send_activation_code_email_task(subject: str, message: str, email: str):
    send_mail(
        subject=subject,
        message=message,
        from_email="suslanchikmopl@gmail.com",
        recipient_list=[email]
    )


@shared_task(name="clear_activation_codes")
def clear_activation_codes():
    now = datetime.now()
    for key in cache.keys("*"):
        if len(key) == 6:
            data = cache.get(key)
            if now >= data['exp']:
                cache.delete(key)
