from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Category, Comment
from django.core.exceptions import ValidationError

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class PostForm(forms.ModelForm):
    new_category = forms.CharField(
        max_length=100, 
        required=False,
        help_text='Create a new category if not found in the list above'
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'status']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
            'status': forms.Select(choices=[
                ('draft', 'Draft'),
                ('published', 'Published')
            ])
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make category field optional
        self.fields['category'].required = False

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        new_category = cleaned_data.get('new_category')

        if not category and not new_category:
            raise forms.ValidationError('Please either select a category or create a new one.')
        
        return cleaned_data

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        min_length=3,
        help_text='Required. 3-30 characters.'
    )
    email = forms.EmailField(
        required=True,
        help_text='Required. Must be a valid email address.'
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        help_text='At least 8 characters.'
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        return password

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user 