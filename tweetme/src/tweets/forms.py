from django import forms

from .models import Tweet

class TweetModelForm(forms.ModelForm):
    content=forms.CharField(label='' ,widget=forms.Textarea(attrs={'placeholder':"Your Message here", "class":"form-control"}))
    class Meta:
        model=Tweet
        fields=[
            #"user",
            "content"
        ]
