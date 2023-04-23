from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #указать поля которые следует создавать
        fields = ['name', 'email', 'body']
        #exclude как альтернатива, указать поля 
        #которые след. игнорировать
        
class SearchForm(forms.Form):
    query = forms.CharField()
