from django import forms

from app_blog.models import Blog, Post


class BlogForm(forms.ModelForm):
    """Форма создания/редактирования объекта app_blog:Blog"""
    class Meta:
        model = Blog
        fields = ("name", )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'custom-field__input',
            'placeholder': ' ',
        })


class PostForm(forms.ModelForm):
    """Форма создания/редактирования объекта app_blog:Post"""
    class Meta:
        model = Post
        fields = ("title", "content", "draft")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class': 'custom-field__input',
            'placeholder': ' ',
        })

        self.fields['content'].widget.attrs.update({
            'class': 'custom-field__input custom-field__input_wide custom-field__input_textarea',
            'placeholder': ' ',
        })
