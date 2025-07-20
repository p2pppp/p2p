from django.core.mail import send_mail
def notify_user_email(user, subject, message):
    send_mail(subject, message, 'no-reply@yourdomain.com', [user.email])

def notify_user_telegram(user, message):
    # используйте user.telegram_id для отправки через Telegram API
