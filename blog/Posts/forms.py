from .models import Blog
from django import forms
from ckeditor_uploader import widgets


class blogForm(forms.Form):
    title = forms.CharField(
        max_length=200, widget=forms.TextInput(attrs={"class": "input",})
    )
    body = forms.CharField(widget=widgets.CKEditorUploadingWidget(), required=False)
    thumbnail = forms.ImageField(allow_empty_file=True, required=False)
