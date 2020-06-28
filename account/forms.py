from django import forms
from .models import RequestVerification, Package, UploadImage


class RequestVerificationForm(forms.ModelForm):
    class Meta:
        model = RequestVerification
        fields = '__all__'
        exclude = ['status']
        labels = {
            'user': "Hello",
            "request_image": "Upload your image"
        }

class CreatePackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = '__all__'
        exclude = ['time']
        labels = {
            'user': "Hello",
        }

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = '__all__'
        labels = {
            'user': 'Hello'
        }