from django  import forms

from advertisement.models import ADPost 


class CreateAdvertisementForm(forms.ModelForm):
    class Meta:
        model = ADPost
        fields = ('title', 'description', 'image')