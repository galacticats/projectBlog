from django import forms
from . import models

class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ["title", "body", "slug", "picture"]


class ArticleEditForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ["body", "picture"]
