from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify 
from django.urls import reverse 
from django.utils import timezone 
from django_countries.fields import CountryField
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"),on_delete=models.CASCADE)
    country = CountryField()
    address = models.CharField(max_length=150, verbose_name=_("Address"),blank=True, null=True)    
    image = models.ImageField(verbose_name=_("Profile Image"), upload_to='profiles/%Y/%m/%d/', blank=True, null=True)
    join_date = models.DateTimeField(verbose_name=_('Joined Date'),default=timezone.now)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)
    

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.slug})

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

