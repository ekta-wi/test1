from django import forms

from .models import Post

#Name of the form is PostForm of type ModelForm
class PostForm(forms.ModelForm):

    class Meta:
#which model does the form expose
        model = Post
#which fields of the model does the form expose. It also makes them required fields
        fields = ('title', 'text',)
