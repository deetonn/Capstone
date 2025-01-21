from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Post, Comment
from .forms import PostForm, CustomUserCreationForm, CommentForm
from django.contrib.auth import login
from django.http import JsonResponse, HttpResponseForbidden

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
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            
            # Set published_date if status is 'published'
            if post.status == 'published':
                post.published_date = timezone.now()
            
            post.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form, 'action': 'Create'})

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
