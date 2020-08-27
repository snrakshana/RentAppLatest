from django import forms

from advertisement.models import ADPost


class CreateAdvertisementForm(forms.ModelForm):
    class Meta:
        model = ADPost
        fields = ('title', 'description', 'image')

class UpdateAdvertisementForm(forms.ModelForm):

    class Meta:
        model = ADPost
        fields = ['title', 'description', 'image']

    def save(self, commit=True):
        ad_post = self.instance
        ad_post.title = self.cleaned_data['title']
        ad_post.description = self.cleaned_data['description']

        if self.cleaned_data['image']:
            ad_post.image = self.cleaned_data['image']

        if commit:
            ad_post.save()
        return ad_post



