from .models import Deal, UserProfile

def admin_stats():
    today_commissions = Deal.objects.filter(
        created_at__date=datetime.date.today()
    ).aggregate(total=models.Sum('commission_buyer') + models.Sum('commission_seller'))
    active_users = UserProfile.objects.filter(is_blocked=False).count()
    return {
        "today_commissions": today_commissions,
        "active_users": active_users,
    }
