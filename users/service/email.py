import datetime

from django.forms import model_to_dict
from django.template.loader import render_to_string
from django.core.cache import cache
import random

from ..tasks.email import send_activation_code_email_task


def generate_code() -> str:
    code_integer = random.randint(0, 999999)
    code_integer_string = str(code_integer)
    return "0" * (6 - len(code_integer_string)) + code_integer_string


def send_email(__user):
    message_subject = "Activate your user account."
    code = generate_code()
    user_data = {
        "user": __user,
        "exp": datetime.datetime.now() + datetime.timedelta(minutes=30)
    }
    cache.set(code, user_data)
    message_content = render_to_string(
        template_name="users/email_activation.html",
        context={
            "user": __user,
            "code": code
        }
    )
    send_activation_code_email_task.apply_async(
        args=[message_subject, message_content, __user['email']]
    )
