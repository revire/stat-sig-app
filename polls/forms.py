from django import forms
from .models import Data, DataFile




class NameForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(), max_length=100)

    class Meta:
        model = Data
        fields = ('post',)


class UploadFileForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

    class Meta:
        model = DataFile
        fields = [
            'file',
            'title'
        ]
