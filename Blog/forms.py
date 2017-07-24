from django import forms
from models import UserModel, PostModel, LikeModel, CommentModel

#created form for signup
class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields=['email','username','name','password']

#created form for login
class LoginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']

#created form for post
class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields=['image', 'caption']

#created form for Like
class LikeForm(forms.ModelForm):

    class Meta:
        model = LikeModel
        fields=['post']

#created form for comment
class CommentForm(forms.ModelForm):

    class Meta:
        model = CommentModel
        fields = ['comment_text', 'post']