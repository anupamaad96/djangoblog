from django import forms
from home.models import Post,Comment

class HomeForm(forms.ModelForm):


    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write something...'

        }
    ))

    class Meta:
        model = Post
        fields = ('post',)


class CommentForm(forms.ModelForm):
    texts = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write comment...'

        }
    ))

    class Meta:
        model = Comment
        fields = ('texts',)
