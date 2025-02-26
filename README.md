﻿# Community Blog Platform (Offline)

A full-stack Django web application that allows users to create, share, and interact with blog posts in a community-driven environment.

## Table of Contents
- [Features](#features)
- [UX Design](#ux-design)
- [Agile Development](#agile-development)
- [Database Schema](#database-schema)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [AI Integration](#ai-integration)
- [Credits](#credits)
- [Technical Documentation](#technical-documentation)

## Live Site: https://deeton-6bef4848d387.herokuapp.com/blog/

## Features

### Existing Features

1. **User Authentication & Authorization**
   - User registration with email verification
   - Role-based access control (regular users and admins)
   - Secure login/logout functionality
   - Password reset capability

2. **Post Management**
   - Create, read, update, and delete blog posts
   - Draft/publish status for posts
   - Rich text editing
   - Category assignment
   - Slug-based URLs for SEO

3. **User Profiles**
   - Customizable user profiles
   - Post history display
   - Activity statistics
   - Author pages

4. **Interactive Elements**
   - Comment system on posts
   - Post categorization
   - User notifications for interactions
   - Responsive search functionality

### Future Features
- Social media sharing
- Post tags
- User following system
- Newsletter integration

## UX Design

### Strategy
The primary goal is to create a community-driven blogging platform that:
- Encourages content creation and sharing
- Provides an intuitive user interface
- Facilitates community interaction
- Ensures content organization and discovery

### User Stories

#### First Time Visitor Goals
1. Understand the platform's purpose
2. Browse existing content easily
3. Register for an account
4. Create their first post

#### Returning Visitor Goals
1. Manage their content
2. Interact with other users' content
3. Track their activity
4. Discover new content

#### Frequent User Goals
1. Build their following
2. Manage multiple posts
3. Engage with the community
4. Access advanced features

### Wireframes
![Wireframe](https://github.com/deetonn/Capstone/blob/main/images/wireframe.png?raw=true "Wireframe")

### Design Choices

#### Color Scheme
  We define the color scheme in the base.html file, using CSS variables.

  The primary color is #1e293b (dark gray);
  The secondary color is #0ea5e9 (light blue);
  The background color is #f8fafc (light gray);
  The text color is #334155 (dark gray);

#### Typography
- Headings: Inter
- Body: System UI
- Monospace: Consolas (for code blocks)

#### Imagery
- Custom icons for actions
- User avatars
- Category images
- Placeholder images

## Agile Development

### Project Management
- Used GitHub Projects for task tracking
- Implemented user stories as issues
- Organized work in weekly sprints
- Regular progress reviews

### User Stories Implementation
[Link to GitHub Projects board](https://github.com/users/deetonn/projects/3)

## Database Schema

### Models

#### User (Django's built-in User model)
- Username
- Email
- Password
- Date joined

#### Post
- Title
- Content
- Author (FK to User)
- Category (FK to Category)
- Status (draft/published)
- Created date
- Published date
- Slug

#### Category
- Name
- Slug
- Description

#### Comment
- Author (FK to User)
- Post (FK to Post)
- Content
- Created date

[Include ERD diagram]

## Technologies Used

### Languages
- HTML5
- CSS3
- JavaScript
- Python 3.11

### Frameworks & Libraries
- Django 4.2
- Bootstrap 5
- Font Awesome
- PostgreSQL
- Whitenoise
- Gunicorn

### Tools
- Git & GitHub
- VS Code
- Heroku
- DrawSQL
- Balsamiq
- Chrome DevTools

## Testing

### Automated Testing
- Unit tests for models
- View testing
- Form validation tests
- Integration tests

### Manual Testing
- User story testing
- Browser compatibility
- Responsive design
- CRUD functionality
- User authentication
- Error handling

### Validation
- HTML (W3C)
- CSS (Jigsaw)
- JavaScript (JSHint)
- Python (PEP8)
- Accessibility (WAVE)
- Performance (Lighthouse)

[Include testing documentation and results]

## Deployment

### Local Development
1. Clone repository
2. Install dependencies
3. Set up environment variables
4. Run migrations
5. Start development server

### Heroku Deployment
1. Create Heroku app
2. Configure environment variables
3. Connect GitHub repository
4. Set up PostgreSQL database
5. Deploy application

### Environment Variables

```python
SECRET_KEY=your_secret_key
DEBUG=False
DATABASE_URL=your_database_url
```


## AI Integration

### Code Generation
- Used GitHub Copilot for:
  - Model structure suggestions
  - View implementations
  - Test case generation

### Debugging
- Leveraged AI for:
  - Error resolution
  - Code optimization
  - Performance improvements

### Testing
- AI-assisted in:
  - Test case design
  - Edge case identification
  - Coverage improvement

## Credits

### Content
- No content was used

### Media
- Emojis from [Emojipedia](https://emojipedia.org/)

### Acknowledgements
- Code Institute tutors
- Mentor support
- Community feedback

## Technical Documentation

### Authentication Pages

#### Login Page (`templates/registration/login.html`)

**Purpose**: Provides secure user authentication with a clean, user-friendly interface.

**Key Features**:
1. Username/email authentication
2. Password field with show/hide toggle
3. "Remember me" functionality
4. Password reset link
5. Registration redirect for new users
6. Form validation with error messages

**Technical Implementation**:
```python
# Uses Django's built-in authentication views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
]
```

**Security Features**:
- CSRF protection enabled
- Password hashing using Django's default PBKDF2 algorithm
- Rate limiting to prevent brute force attacks
- Session management with secure cookies
- SQL injection protection through Django's ORM

**Form Validation**:
- Username/email format validation
- Password complexity requirements
- Custom error messages for invalid credentials
- Cross-site request forgery (CSRF) token validation

**User Experience**:
- Responsive design for all screen sizes
- Clear error messaging
- Loading states during authentication
- Automatic redirect to previous page after login
- Session persistence option

**CSS Styling**:
```css
.login-container {
    max-width: 400px;
    margin: 2rem auto;
    padding: 2rem;
    background: white;
    border-radius: 12px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.form-group {
    margin-bottom: 1.5rem;
}

.password-toggle {
    position: relative;
    display: flex;
    align-items: center;
}

.error-message {
    color: var(--error-color);
    font-size: 0.875rem;
    margin-top: 0.5rem;
}
```

**JavaScript Functionality**:
```javascript
// Password visibility toggle
function togglePasswordVisibility() {
    const passwordInput = document.getElementById('password');
    const toggleIcon = document.getElementById('togglePassword');
    
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        toggleIcon.classList.replace('fa-eye', 'fa-eye-slash');
    } else {
        passwordInput.type = 'password';
        toggleIcon.classList.replace('fa-eye-slash', 'fa-eye');
    }
}
```

**Testing**:
```python
def test_login_view(self):
    response = self.client.get(reverse('login'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'registration/login.html')

def test_login_functionality(self):
    response = self.client.post(reverse('login'), {
        'username': 'testuser',
        'password': 'testpass123'
    })
    self.assertRedirects(response, reverse('blog:home'))
```

**Accessibility Features**:
- ARIA labels for form inputs
- Keyboard navigation support
- High contrast text
- Clear focus states
- Screen reader compatibility

**Error Handling**:
1. Invalid credentials
2. Account lockout after failed attempts
3. Network connectivity issues
4. Session timeout
5. Browser compatibility issues

**Performance Optimizations**:
- Minimal DOM manipulation
- Efficient CSS selectors
- Optimized image assets
- Cached template rendering
- Minified static files

#### Registration Page (`templates/registration/register.html`)

**Purpose**: Enables new users to create accounts with secure validation and a streamlined onboarding process.

**Key Features**:
1. Username availability check
2. Email validation
3. Password strength requirements
4. Terms of service acceptance
5. Email verification (optional)
6. Anti-spam protection

**Technical Implementation**:
```python
class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'form': form})
    
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('blog:home')
        return render(request, 'registration/register.html', {'form': form})
```

**Form Validation**:
- Username requirements:
  - Unique
  - 3-30 characters
  - Alphanumeric with underscores
- Password requirements:
  - Minimum 8 characters
  - At least one number
  - At least one special character
  - Cannot be similar to username
- Email validation:
  - Valid email format
  - Unique in system
  - Domain verification

**Security Features**:
- Password hashing with Django's PBKDF2
- CSRF protection
- Rate limiting for registration attempts
- Honeypot fields for bot prevention
- Secure session handling

**User Experience**:
- Real-time validation feedback
- Password strength indicator
- Clear error messaging
- Progressive form completion
- Success confirmation
- Automatic login after registration

**CSS Styling**:
```css
.register-container {
    max-width: 500px;
    margin: 3rem auto;
    padding: 2rem;
    background: white;
    border-radius: 12px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.form-header {
    text-align: center;
    margin-bottom: 2rem;
}

.password-strength {
    height: 4px;
    margin-top: 0.5rem;
    border-radius: 2px;
    transition: all 0.3s ease;
}

.strength-weak {
    background: var(--error-color);
    width: 33%;
}

.strength-medium {
    background: var(--warning-color);
    width: 66%;
}

.strength-strong {
    background: var(--success-color);
    width: 100%;
}

.validation-message {
    font-size: 0.875rem;
    margin-top: 0.25rem;
}

.validation-success {
    color: var(--success-color);
}

.validation-error {
    color: var(--error-color);
}
```

**JavaScript Functionality**:
```javascript
// Real-time username availability check
async function checkUsername(username) {
    const response = await fetch(`/api/check-username/?username=${username}`);
    const data = await response.json();
    return data.available;
}

// Password strength checker
function checkPasswordStrength(password) {
    let strength = 0;
    if (password.length >= 8) strength++;
    if (/[0-9]/.test(password)) strength++;
    if (/[A-Z]/.test(password)) strength++;
    if (/[^A-Za-z0-9]/.test(password)) strength++;
    return strength;
}

// Update UI based on password strength
function updatePasswordStrength(strength) {
    const indicator = document.querySelector('.password-strength');
    indicator.className = 'password-strength';
    if (strength >= 4) indicator.classList.add('strength-strong');
    else if (strength >= 2) indicator.classList.add('strength-medium');
    else indicator.classList.add('strength-weak');
}
```

**Testing**:
```python
class RegistrationTests(TestCase):
    def test_registration_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_successful_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'TestPass123!',
            'password2': 'TestPass123!'
        })
        self.assertEqual(User.objects.count(), 1)
        self.assertRedirects(response, reverse('blog:home'))

    def test_invalid_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'a',  # too short
            'password1': 'short'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'username', 
                           'Username must be at least 3 characters long.')
```

**Accessibility Features**:
- Semantic HTML structure
- Form labels and ARIA attributes
- Error announcements for screen readers
- Keyboard navigation support
- Focus management
- Color contrast compliance

**Error Handling**:
1. Duplicate username/email
2. Invalid form submissions
3. Password mismatch
4. Network connectivity issues
5. Server-side validation failures
6. Rate limit exceeded
7. Email verification failures

**Performance Considerations**:
- Debounced username availability checks
- Lazy loading of validation scripts
- Client-side validation before submission
- Optimized form rendering
- Efficient database queries
- Caching of static assets

#### Categories Page (`blog/templates/blog/categories.html`)

**Purpose**: Provides an organized overview of all blog categories with post counts and descriptions, enabling easy content discovery.

**Key Features**:
1. Grid layout of category cards
2. Post count per category
3. Category descriptions
4. Interactive hover effects
5. Direct links to filtered post lists
6. Responsive design

**Technical Implementation**:
```python
def categories_list(request):
    categories = Category.objects.annotate(
        post_count=Count('post')
    ).order_by('-post_count')
    
    return render(request, 'blog/categories.html', {
        'categories': categories
    })
```

**Data Structure**:
- Category Model fields used:
  - name: Category title
  - slug: URL-friendly identifier
  - description: Category details
  - post_count: Annotated count of posts

**User Experience**:
- Clean grid layout
- Visual feedback on interaction
- Clear category descriptions
- Easy navigation to category posts
- Post count indicators
- Smooth animations

**CSS Styling**:
```css
.categories-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
}

.category-card {
    background: white;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    transition: all 0.2s ease;
}

.category-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.view-posts i {
    transition: transform 0.2s ease;
}

.category-card:hover .view-posts i {
    transform: translateX(4px);
}
```

**Performance Optimizations**:
- Database optimization:
  - Annotated queries to avoid N+1 problems
  - Efficient post counting
- Frontend performance:
  - CSS Grid for responsive layout
  - Hardware-accelerated animations
  - Lazy loading of category descriptions

**Testing**:
```python
class CategoryTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Test Category',
            slug='test-category',
            description='Test Description'
        )
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=self.user,
            category=self.category
        )

    def test_categories_list_view(self):
        response = self.client.get(reverse('blog:categories'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/categories.html')
        self.assertContains(response, 'Test Category')
        self.assertContains(response, '1 posts')

    def test_category_filtering(self):
        response = self.client.get(f'/blog/explore/?category={self.category.slug}')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
```

**Accessibility Features**:
- Semantic HTML structure
- Proper heading hierarchy
- ARIA labels for interactive elements
- Sufficient color contrast
- Keyboard navigation support
- Screen reader-friendly content

**Error Handling**:
1. Empty categories display
2. Long category names
3. Missing descriptions
4. Zero post count display
5. Invalid category slugs

**Security Considerations**:
- XSS prevention in category names/descriptions
- SQL injection protection
- CSRF protection for any forms
- Input sanitization
- URL parameter validation

**Responsive Design**:
- Grid adapts to screen size
- Mobile-friendly touch targets
- Readable text at all breakpoints
- Maintained functionality across devices
- Optimized spacing for different screens

#### Explore Page (`blog/templates/blog/explore.html`)

**Purpose**: Provides an intelligent content discovery system with personalized recommendations and advanced search capabilities.

**Key Features**:
1. Advanced search functionality
2. Category filtering
3. Multiple sorting options
4. Personalized recommendations
5. Post matching algorithm
6. Reading time estimation
7. Interactive post cards

**Technical Implementation**:
```python
# blog/views.py
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
```

**Recommendation Algorithm**:
The explore page implements a sophisticated post matching algorithm that calculates a match score (0-100) based on:
- Category Match (+50 points): Post is in a category the user has written in
- Author Interaction (+25 points): User has commented on posts by this author
- Recency (+25 points): Post was published within the last 7 days

**Search and Filtering**:
- Full-text search across:
  - Post titles
  - Post content
  - Author usernames
- Category filtering with post counts
- Sorting options:
  - Latest (default)
  - Alphabetical (A-Z)
  - Most Popular (by comment count)

**User Experience**:
- Visual match indicators:
  - Perfect Match (≥75 points): Star icon
  - Good Match (≥50 points): Thumbs up icon
  - Similar (<50 points): Outline star icon
- Reading time estimation (200 words/minute)
- Comment count display
- Post metadata display
- Responsive card layout

**CSS Styling**:
```css
.explore-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 0 1rem;
}

.post-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    padding: 1.25rem;
    transition: all 0.2s ease;
}

.match-score {
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.875rem;
}

.match-score.high {
    background: #ecfdf5;
    color: #059669;
}

.match-score.medium {
    background: #fef3c7;
    color: #d97706;
}

.match-score.low {
    background: #f1f5f9;
    color: #64748b;
}
```

**Performance Optimizations**:
- Efficient database queries:
  - Annotated comment counts
  - Selected related fields
  - Cached category counts
- Frontend optimizations:
  - Lazy loading of images
  - Debounced search input
  - CSS transitions for smooth interactions
  - Responsive image sizing

**Testing**:
```python
class ExploreViewTests(TestCase):
    def setUp(self):
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
            status='published'
        )

    def test_explore_view_search(self):
        response = self.client.get('/blog/explore/?q=test')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_explore_view_filtering(self):
        response = self.client.get(f'/blog/explore/?category={self.category.slug}')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_recommendation_algorithm(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/blog/explore/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Recommended for You')
```

**Accessibility Features**:
- ARIA labels for interactive elements
- Semantic HTML structure
- Color contrast compliance
- Keyboard navigation support
- Screen reader-friendly content
- Focus management

**Error Handling**:
1. No results found state
2. Invalid search queries
3. Invalid category slugs
4. Sort parameter validation
5. Empty recommendation handling
6. Network error states

**Mobile Responsiveness**:
- Fluid grid layouts
- Adaptive card designs
- Touch-friendly interface
- Optimized spacing
- Readable typography
- Collapsible filters

#### Drafts Page (`blog/templates/blog/my_drafts.html`)

**Purpose**: Provides users with a dedicated space to manage their unpublished posts, offering quick access to edit, publish, or delete draft content.

**Key Features**:
1. Draft post listing
2. Last modified timestamps
3. Content previews
4. Category display
5. Quick action buttons
6. Empty state handling

**Technical Implementation**:
```python
@login_required
def my_drafts(request):
    drafts = Post.objects.filter(
        author=request.user,
        status='draft'
    ).order_by('-updated_date')
    
    return render(request, 'blog/my_drafts.html', {
        'drafts': drafts
    })

@login_required
def publish_post(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    
    if request.method == 'POST':
        post.status = 'published'
        post.published_date = timezone.now()
        post.save()
        messages.success(request, 'Post published successfully!')
        return redirect('blog:post_detail', slug=post.slug)
```

**User Interface Components**:
1. Draft Cards:
   - Title
   - Last modified date
   - Content preview
   - Category indicator
   - Action buttons
2. Empty State:
   - Friendly message
   - Create post button
   - Descriptive icon

**JavaScript Functionality**:
```javascript
async function publishPost(slug) {
    if (confirm('Are you sure you want to publish this post?')) {
        try {
            const response = await fetch(`/blog/post/${slug}/publish/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                }
            });
            
            if (response.ok) {
                window.location.reload();
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error publishing post');
        }
    }
}

async function deletePost(slug) {
    if (confirm('Are you sure you want to delete this draft? This cannot be undone.')) {
        // Similar implementation to publishPost
    }
}
```

**CSS Styling**:
```css
.draft-card {
    background: white;
    border-radius: 12px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    margin-bottom: 1rem;
    transition: transform 0.2s ease;
}

.action-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    font-size: 0.9rem;
    cursor: pointer;
    transition: all 0.2s ease;
}

.edit-btn {
    background: #f1f5f9;
    color: #0284c7;
}

.publish-btn {
    background: #f0fdf4;
    color: #16a34a;
}

.delete-btn {
    background: #fef2f2;
    color: #dc2626;
}
```

**Security Features**:
- Login required decorator
- Author verification
- CSRF protection
- Confirmation dialogs
- Secure API endpoints

**Testing**:
```python
class DraftTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.draft = Post.objects.create(
            title='Test Draft',
            content='Draft Content',
            author=self.user,
            status='draft'
        )

    def test_drafts_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('blog:my_drafts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Draft')

    def test_publish_draft(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('blog:publish_post', args=[self.draft.slug])
        )
        self.draft.refresh_from_db()
        self.assertEqual(self.draft.status, 'published')
```

**Error Handling**:
1. Failed publish attempts
2. Failed delete operations
3. Network connectivity issues
4. Invalid draft access
5. Unauthorized actions

**Accessibility Features**:
- Semantic HTML structure
- ARIA labels for buttons
- Keyboard navigation
- Focus management
- Screen reader support
- High contrast text

**Performance Optimizations**:
- Efficient database queries
- Optimized JavaScript
- Minimal DOM updates
- Lazy loading
- CSS transitions
- Debounced actions

**Mobile Responsiveness**:
- Fluid layouts
- Touch-friendly buttons
- Readable text sizes
- Appropriate spacing
- Adaptive card design
- Optimized for small screens

#### Post Detail Page (`blog/templates/blog/post_detail.html`)

**Purpose**: Displays the full content of a blog post with interactive comments section, author controls, and metadata.

**Key Features**:
1. Post Content Display:
   - Title and category
   - Author information
   - Publication date
   - Reading time estimate
   - Comment count
   - Full post content

2. Author Controls:
   - Edit post button
   - Delete post button
   - Access control verification

3. Comments System:
   - Comment submission
   - Comment editing
   - Comment deletion
   - Login prompt for non-authenticated users

**Technical Implementation**:
```python
@login_required
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    comments = post.comments.order_by('-created_date')
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog:post_detail', slug=slug)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })
```

**Interactive Features**:
1. Comment Management:
```javascript
async function editComment(commentId) {
    const commentDiv = document.getElementById(`comment-${commentId}`);
    const content = commentDiv.querySelector('.comment-content p').textContent;
    
    const form = document.createElement('div');
    form.className = 'edit-form';
    form.innerHTML = `
        <textarea rows="3">${content}</textarea>
        <div class="edit-form-buttons">
            <button onclick="saveComment(${commentId})" class="submit-button">Save</button>
            <button onclick="cancelEdit(${commentId})" class="action-btn">Cancel</button>
        </div>
    `;
    // ... rest of implementation
}

async function deleteComment(commentId) {
    if (confirm('Are you sure you want to delete this comment?')) {
        try {
            const response = await fetch(`/blog/comment/${commentId}/delete/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                }
            });
            // ... handle response
        } catch (error) {
            console.error('Error:', error);
        }
    }
}
```

**CSS Styling**:
```css
.post-detail {
    max-width: 800px;
    margin: 2rem auto;
    padding: 3rem;
    background: white;
    border-radius: 16px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.post-header {
    text-align: center;
    margin-bottom: 3rem;
}

.comments-section {
    margin-top: 3rem;
    padding-top: 2rem;
    border-top: 1px solid #eee;
}

.comment {
    background: white;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    transition: transform 0.2s ease;
}
```

**Security Features**:
1. Authentication checks for:
   - Comment creation
   - Comment editing
   - Comment deletion
   - Post editing
2. CSRF protection
3. XSS prevention
4. Input sanitization
5. Author verification

**Performance Optimizations**:
1. Efficient comment loading
2. Optimized DOM updates
3. Smooth animations
4. Lazy loading
5. Debounced actions
6. Minimal server requests

**Accessibility Features**:
- Semantic HTML structure
- ARIA labels
- Keyboard navigation
- Focus management
- Screen reader compatibility
- Color contrast compliance

**Error Handling**:
1. Failed comment submissions
2. Network errors
3. Invalid permissions
4. Delete confirmations
5. Edit validations
6. Form validation

**Mobile Responsiveness**:
```css
@media (max-width: 768px) {
    .post-detail {
        padding: 1.5rem;
        margin: 1rem;
        border-radius: 12px;
    }

    .post-header h1 {
        font-size: 2rem;
    }

    .post-meta {
        flex-direction: column;
        gap: 1rem;
        align-items: center;
    }
}
```

**Testing**:
```python
class PostDetailTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=self.user,
            status='published'
        )

    def test_post_detail_view(self):
        response = self.client.get(
            reverse('blog:post_detail', args=[self.post.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_comment_creation(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('blog:post_detail', args=[self.post.slug]),
            {'content': 'Test Comment'}
        )
        self.assertEqual(self.post.comments.count(), 1)
```

#### Post Form Page (`blog/templates/blog/post_form.html`)

**Purpose**: Provides a user-friendly interface for creating and editing blog posts with real-time validation and category management.

**Key Features**:
1. Dynamic Form Handling:
   - Post creation
   - Post editing
   - Category selection/creation
   - Status management
   - Validation feedback

2. Form Components:
   - Title input
   - Content editor
   - Category selector
   - New category creation
   - Post status toggle
   - Action buttons

**Technical Implementation**:
```python
class PostForm(forms.ModelForm):
    new_category = forms.CharField(required=False)
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'status']
        
    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        new_category = cleaned_data.get('new_category')
        
        if not category and not new_category:
            raise ValidationError('Please either select a category or create a new one')
```

**Form Validation**:
- Required fields:
  - Title (3-200 characters)
  - Content (minimum 10 characters)
  - Category (existing or new)
- Status options:
  - Draft
  - Published
- Error handling:
  - Field-specific errors
  - Form-level validation
  - Real-time feedback

**CSS Styling**:
```css
.post-form-container {
    max-width: 800px;
    margin: 2rem auto;
    padding: 3rem;
    background: white;
    border-radius: 16px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.form-group input[type="text"],
.form-group textarea,
.form-group select {
    padding: 0.875rem;
    border: 2px solid #e2e8f0;
    border-radius: 8px;
    font-size: 1rem;
    transition: all 0.3s ease;
    background: #f8fafc;
}

.submit-button {
    background: var(--secondary-color);
    color: white;
    border: none;
    flex: 1;
    padding: 0.875rem 1.75rem;
    border-radius: 8px;
    transition: all 0.3s ease;
}
```

**User Experience Features**:
1. Visual Feedback:
   - Input focus states
   - Error highlighting
   - Success messages
   - Loading states
2. Form Navigation:
   - Tabindex ordering
   - Keyboard shortcuts
   - Cancel option
   - Save confirmation

**Security Features**:
- CSRF protection
- Input sanitization
- XSS prevention
- Authentication checks
- Permission validation
- Data validation

**Testing**:
```python
class PostFormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.category = Category.objects.create(
            name='Test Category',
            slug='test-category'
        )

    def test_valid_post_creation(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('blog:post_create'), {
            'title': 'Test Post',
            'content': 'Test Content',
            'category': self.category.id,
            'status': 'draft'
        })
        self.assertEqual(Post.objects.count(), 1)

    def test_new_category_creation(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('blog:post_create'), {
            'title': 'Test Post',
            'content': 'Test Content',
            'new_category': 'New Category',
            'status': 'draft'
        })
        self.assertTrue(Category.objects.filter(name='New Category').exists())
```

**Accessibility Features**:
- Semantic form structure
- ARIA labels
- Error announcements
- Focus management
- Keyboard navigation
- Color contrast compliance
- Screen reader support

**Error Handling**:
1. Form validation errors
2. Category creation failures
3. Network connectivity issues
4. Session timeouts
5. Permission denied states
6. Unsaved changes warnings

**Mobile Responsiveness**:
```css
@media (max-width: 768px) {
    .post-form-container {
        margin: 1rem;
        padding: 1.5rem;
    }

    .form-header h1 {
        font-size: 2rem;
    }

    .form-actions {
        flex-direction: column;
    }

    .submit-button,
    .cancel-button {
        width: 100%;
        justify-content: center;
    }
}
```

**Performance Optimizations**:
- Debounced validation
- Optimized form submission
- Lazy loading components
- Efficient DOM updates
- Minimal server requests
- Cached form data

#### Profile Page (`blog/templates/blog/profile.html`)

**Purpose**: Displays user profile information, activity statistics, recent content, and category engagement in an organized dashboard layout.

**Key Features**:
1. Profile Overview:
   - Username display
   - Join date
   - Activity statistics
   - Avatar placeholder

2. Statistics Dashboard:
   - Published posts count
   - Total comments
   - Active categories
   - Visual stat cards

3. Recent Activity:
   - Latest posts
   - Recent comments
   - Post status indicators
   - Category distribution

**Technical Implementation**:
```python
def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    
    stats = {
        'join_date': profile_user.date_joined,
        'published_posts': Post.objects.filter(
            author=profile_user, 
            status='published'
        ).count(),
        'total_comments': Comment.objects.filter(
            author=profile_user
        ).count()
    }
    
    recent_posts = Post.objects.filter(
        author=profile_user
    ).order_by('-created_date')[:5]
    
    recent_comments = Comment.objects.filter(
        author=profile_user
    ).select_related('post').order_by('-created_date')[:5]
    
    active_categories = Category.objects.filter(
        post__author=profile_user
    ).annotate(
        post_count=Count('post')
    ).order_by('-post_count')
    
    return render(request, 'blog/profile.html', {
        'profile_user': profile_user,
        'stats': stats,
        'recent_posts': recent_posts,
        'recent_comments': recent_comments,
        'active_categories': active_categories
    })
```

**CSS Styling**:
```css
.profile-page {
    max-width: var(--container-width);
    margin: 0 auto;
    padding: 2rem 1rem;
}

.profile-content {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 2rem;
}

.activity-card {
    background: #f8fafc;
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
    transition: all 0.2s ease;
}

.status-badge {
    font-size: 0.75rem;
    padding: 0.25rem 0.75rem;
    border-radius: 999px;
    font-weight: 500;
    text-transform: capitalize;
}

.status-badge.published {
    background: #dcfce7;
    color: #166534;
}

.status-badge.draft {
    background: #f1f5f9;
    color: #475569;
}
```

**Component Structure**:
1. Profile Header:
   - User information
   - Join date display
   - Statistics grid
2. Activity Section:
   - Recent posts list
   - Comment history
   - Empty state handling
3. Categories Section:
   - Active categories grid
   - Post count per category
   - Category navigation links

**Interactive Features**:
- Hover effects on cards
- Status indicators
- Category filtering
- Post/comment linking
- Responsive layout
- Dynamic content loading

**Performance Optimizations**:
1. Database Queries:
   - Selected related fields
   - Annotated counts
   - Limited result sets
2. Frontend:
   - CSS Grid layout
   - Smooth transitions
   - Lazy loading
   - Efficient DOM structure

**Accessibility Features**:
- Semantic HTML structure
- ARIA labels
- Color contrast compliance
- Focus management
- Screen reader support
- Keyboard navigation

**Mobile Responsiveness**:
```css
@media (max-width: 768px) {
    .profile-content {
        grid-template-columns: 1fr;
    }

    .profile-info {
        flex-direction: column;
        text-align: center;
        gap: 1rem;
    }

    .stats-grid {
        grid-template-columns: 1fr;
    }

    .activity-section {
        padding: 1.5rem;
    }
}
```

**Error States**:
1. Empty States:
   - No recent posts
   - No comments
   - No categories
2. Loading States:
   - Content skeleton
   - Lazy loading
   - Progressive enhancement

**Testing**:
```python
class ProfileViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=self.user,
            status='published'
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='Test Comment'
        )

    def test_profile_view(self):
        response = self.client.get(
            reverse('blog:profile', args=['testuser'])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'Test Comment')
```
