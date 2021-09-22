from django.forms import ModelForm
from .models import Sample

#Form for uploading samples to model
class SampleForm(ModelForm):
    class Meta:
        model = Sample
        fields = ['attachment']