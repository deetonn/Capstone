from .models import Category
from django.db.models import Count

def categories_processor(request):
    categories = Category.objects.annotate(
        post_count=Count('post')
    ).order_by('-post_count')
    return {'header_categories': categories} 