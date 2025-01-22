from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Category
from django.utils import timezone

# Create your tests here.

class BlogTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.category = Category.objects.create(
            name='Test Category',
            slug='test-category'
        )
        self.post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=self.user,
            category=self.category,
            status='published',
            slug='test-post',
            published_date=timezone.now()
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        response = self.client.get(reverse('blog:post_detail', args=['test-post']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
        self.assertContains(response, 'Test Post')

    def test_create_post(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('blog:post_create'), {
            'title': 'New Test Post',
            'content': 'New Test Content',
            'category': self.category.id,
            'status': 'published'
        })
        self.assertEqual(Post.objects.count(), 2)
