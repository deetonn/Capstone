from django.db import migrations

def add_default_categories(apps, schema_editor):
    Category = apps.get_model('blog', 'Category')
    
    default_categories = [
        {
            'name': 'Technology',
            'slug': 'technology',
            'description': 'Posts about programming, software, hardware, and tech news'
        },
        {
            'name': 'Personal Growth',
            'slug': 'personal-growth',
            'description': 'Self-improvement, productivity, and life lessons'
        },
        {
            'name': 'Creative Writing',
            'slug': 'creative-writing',
            'description': 'Stories, poems, and creative expressions'
        },
        {
            'name': 'Science',
            'slug': 'science',
            'description': 'Scientific discoveries, research, and explanations'
        },
        {
            'name': 'Travel',
            'slug': 'travel',
            'description': 'Travel experiences, tips, and destination guides'
        },
        {
            'name': 'Health & Wellness',
            'slug': 'health-wellness',
            'description': 'Physical health, mental health, and well-being'
        },
        {
            'name': 'Arts & Culture',
            'slug': 'arts-culture',
            'description': 'Art, music, movies, and cultural discussions'
        },
        {
            'name': 'Career & Work',
            'slug': 'career-work',
            'description': 'Professional development, work life, and career advice'
        },
        {
            'name': 'Food & Cooking',
            'slug': 'food-cooking',
            'description': 'Recipes, cooking tips, and food experiences'
        },
        {
            'name': 'Gaming',
            'slug': 'gaming',
            'description': 'Video games, board games, and gaming culture'
        },
        {
            'name': 'Books & Reading',
            'slug': 'books-reading',
            'description': 'Book reviews, reading lists, and literary discussions'
        },
        {
            'name': 'Opinion',
            'slug': 'opinion',
            'description': 'Personal views, commentary, and discussions'
        }
    ]

    for category_data in default_categories:
        Category.objects.get_or_create(
            slug=category_data['slug'],
            defaults={
                'name': category_data['name'],
                'description': category_data['description']
            }
        )

def remove_default_categories(apps, schema_editor):
    Category = apps.get_model('blog', 'Category')
    Category.objects.filter(slug__in=[
        'technology', 'personal-growth', 'creative-writing', 
        'science', 'travel', 'health-wellness', 'arts-culture',
        'career-work', 'food-cooking', 'gaming', 'books-reading',
        'opinion'
    ]).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),  # Replace with your last migration
    ]

    operations = [
        migrations.RunPython(add_default_categories, remove_default_categories),
    ] 