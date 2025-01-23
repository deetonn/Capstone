from blog.models import Category
from django.db.models import Count

def categories_processor(request):
    top_categories = Category.objects.annotate(
        post_count=Count('post')
    ).order_by('-post_count')[:3]  # Get top 3 by post count
    return {'header_categories': list(top_categories)}

def notification_count(request):
    if request.user.is_authenticated:
        try:
            unread_count = request.user.notifications.filter(read=False).count()
            return {'unread_notifications_count': unread_count}
        except:
            return {'unread_notifications_count': 0}
    return {'unread_notifications_count': 0} 