from django.conf import settings
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from .models import User
from django.utils.html import strip_tags

def send_email(user):
    
    if 'model_state' in user:
        del user['model_state']

    user = User.objects.get(pk = user["id"])
    
    current_site = settings.SITE_NAME
    email_subject = 'Активируйте ваш аккаунт'

    html_message = render_to_string('users/account_activation_email.html', {
            'user': user.__str__,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
            })
    
    plain_message = strip_tags(html_message)
        
    send_mail(email_subject, plain_message, "birzha@nsuem.ru", [user.email], fail_silently=False, html_message=html_message)


    

    