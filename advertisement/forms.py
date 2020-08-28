from django import forms

from advertisement.models import ADPost


class CreateAdvertisementForm(forms.ModelForm):
    
    class Meta:
        model = ADPost
        fields = ('title', 'description', 'image','district','price','city','is_negotiable','fuel_type','transmission','body_type','vehicle_model','vehicle_brand')
        

        

class UpdateAdvertisementForm(forms.ModelForm):

    class Meta: 
        model = ADPost
        fields = ('title', 'description', 'image','district','price','city','is_negotiable','fuel_type','transmission','body_type','vehicle_model','vehicle_brand')

    def save(self, commit=True):
        ad_post = self.instance
        ad_post.title = self.cleaned_data['title']
        ad_post.description = self.cleaned_data['description']
        ad_post.district = self.cleaned_data['district']
        ad_post.price = self.cleaned_data['price']
        ad_post.city = self.cleaned_data['city']
        ad_post.is_negotiable = self.cleaned_data['is_negotiable']
        ad_post.fuel_type = self.cleaned_data['fuel_type']
        ad_post.transmission = self.cleaned_data['transmission']
        ad_post.body_type = self.cleaned_data['body_type']
        ad_post.vehicle_model = self.cleaned_data['vehicle_model']
        ad_post.vehicle_brand = self.cleaned_data['vehicle_brand']
        

        if self.cleaned_data['image']:
            ad_post.image = self.cleaned_data['image']

        if commit:
            ad_post.save()
        return ad_post



