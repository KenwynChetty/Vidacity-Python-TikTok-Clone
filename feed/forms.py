from django import forms
from feed.models import Post 

class NewPostForm(forms.ModelForm):
    files =  forms.FileField(widget=forms.FileInput(attrs={'type':'file','id':'input-tag', 'accept':'video/*'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'input', 'placeholder':'Enter Your Post Description', 'rows':'7'}))
    tags = forms.CharField(widget=forms.TextInput(attrs={'class':'tags','placeholder':'Enter #HashTags'}))

    class Meta:
        model = Post
        fields = ['files','description','tags']