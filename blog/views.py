from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Post, Comment, Category
from .forms import PostForm, CustomUserCreationForm, CommentForm
from django.contrib.auth import login
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib import messages
from django.db.models import Q, Count

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(
        status='published',
        published_date__isnull=False
    ).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid() and request.user.is_authenticated:
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'new_comment': new_comment
    })

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            
            # Handle new category creation
            new_category = form.cleaned_data.get('new_category')
            if new_category:
                category, created = Category.objects.get_or_create(
                    name=new_category,
                    defaults={'slug': slugify(new_category)}
                )
                post.category = category
            
            post.author = request.user
            post.slug = slugify(post.title)
            
            # Set published_date if status is 'published'
            if post.status == 'published':
                post.published_date = timezone.now()
            
            post.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm()
    
    return render(request, 'blog/post_form.html', {
        'form': form,
        'action': 'Create',
        'categories': Category.objects.all()
    })

@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.author != request.user:
        return HttpResponseForbidden("You cannot edit this post")
        
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            
            # Handle published_date based on status changes
            if post.status == 'published' and not post.published_date:
                post.published_date = timezone.now()
            elif post.status == 'draft':
                post.published_date = None
                
            post.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'action': 'Edit'})

@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.author != request.user:
        return HttpResponseForbidden("You cannot delete this post")
        
    if request.method == "POST":
        post.delete()
        return redirect('blog:post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:post_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    # Check if user owns the comment
    if comment.author != request.user:
        return HttpResponseForbidden("You cannot edit this comment")
    
    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            comment.content = content
            comment.save()
            return JsonResponse({
                'success': True,
                'content': comment.content
            })
    return JsonResponse({'success': False}, status=400)

@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    # Check if user owns the comment
    if comment.author != request.user:
        return HttpResponseForbidden("You cannot delete this comment")
    
    post_slug = comment.post.slug
    comment.delete()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': True})
    return redirect('blog:post_detail', slug=post_slug)

def explore(request):
    # Get search query
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    sort = request.GET.get('sort', '-published_date')

    # Base queryset
    posts = Post.objects.filter(status='published')

    # Apply search if provided
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__username__icontains=query)
        )

    # Apply category filter
    if category:
        posts = posts.filter(category__slug=category)

    # Apply sorting
    valid_sorts = {
        '-published_date': '-published_date',
        'title': 'title',
        'popular': '-comments__count',
    }
    posts = posts.annotate(comments_count=Count('comments')).order_by(valid_sorts.get(sort, '-published_date'))

    # Get personalized recommendations if user is logged in
    recommended_posts = []
    if request.user.is_authenticated:
        # Get user's interests based on their posts and interactions
        user_categories = Post.objects.filter(
            author=request.user
        ).values_list('category', flat=True).distinct()
        
        # Calculate match score for each post
        for post in posts:
            match_score = 0
            # Same category as user's posts
            if post.category_id in user_categories:
                match_score += 50
            # Same author as posts user has commented on
            if Comment.objects.filter(
                author=request.user,
                post__author=post.author
            ).exists():
                match_score += 25
            # Recent post
            if post.published_date and (timezone.now() - post.published_date).days < 7:
                match_score += 25
            
            post.match_score = match_score

        recommended_posts = Post.objects.filter(
            category__in=user_categories
        ).exclude(
            author=request.user
        ).order_by('-published_date')[:5]

    # Get all categories for filter
    categories = Category.objects.annotate(post_count=Count('post'))

    context = {
        'posts': posts,
        'recommended_posts': recommended_posts,
        'categories': categories,
        'query': query,
        'selected_category': category,
        'selected_sort': sort,
    }
    
    return render(request, 'blog/explore.html', context)
