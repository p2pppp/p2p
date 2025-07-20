from celery import shared_task
from .models import Deal
import datetime

@shared_task
def auto_cancel_old_deals():
    threshold = datetime.datetime.now() - datetime.timedelta(minutes=30)
    deals = Deal.objects.filter(status="created", created_at__lt=threshold)
    for deal in deals:
        deal.status = "cancelled"
        deal.save()
