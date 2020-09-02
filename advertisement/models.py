from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver




def upload_location(instance, filename):
	file_path = 'ad/{author_id}/{title}-{filename}'.format(
				author_id=str(instance.author.id),title=str(instance.title), filename=filename)
	return file_path


class ADPost(models.Model):
	choice_district = [
		  ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
    ),
    ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
    ),
    ('unknown', 'Unknown'),
	]

	choice_city = [
			('vinyl', 'Vinyl'),
            ('cd', 'CD'),
	]

	choice_type = [

	]

	fuel_type = [
		('vinyl', 'Vinyl'),
	]

	body_type = [
		('vinyl', 'Vinyl'),
	]

	transmission = [
		('vinyl', 'Vinyl'),
	]

	fuel_type = [
		('vinyl', 'Vinyl'),
	]


	title 					= models.CharField(max_length=50)
	price					= models.DecimalField(max_digits=6,decimal_places=2)
	district 				= models.CharField(max_length=100, choices=choice_district, null=True)
	city					= models.CharField(max_length=100,blank=True,choices=choice_city)
	image		 			= models.ImageField(upload_to=upload_location, null=True)
	vehicle_brand 			= models.CharField(max_length=200, null=True)
	vehicle_model			= models.CharField(max_length=200,null=True, blank=True)
	body_type				= models.CharField(max_length=200,choices=body_type, null=True )
	transmission			= models.CharField(max_length=100,choices=transmission,null=True)
	fuel_type				= models.CharField(max_length=200, choices=fuel_type,null=True)
	is_negotiable			= models.BooleanField(default=False)
	description 			= models.TextField(max_length=5000, null=False, blank=False )
	date_published 			= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated 			= models.DateTimeField(auto_now=True, verbose_name="date updated")
	author 					= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	slug 					= models.SlugField(blank=True, unique=True)
	

	def __str__(self):
		return f"{self.title}"


@receiver(post_delete, sender=ADPost)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 



def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.author.username + "-" + instance.title)

pre_save.connect(pre_save_blog_post_receiver, sender=ADPost)



