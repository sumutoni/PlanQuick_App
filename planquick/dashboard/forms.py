from django import forms

class UploadForm(forms.Form):
    #file upload form
    file = forms.FileField()
