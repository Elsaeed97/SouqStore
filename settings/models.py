from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Brand(models.Model):
     BRDName = models.CharField(verbose_name=_("Name"), max_length=50)
     BRDDesc = models.TextField(verbose_name=_("Description"),blank=True, null=True)
    

     class Meta:
          verbose_name = _("Brand")
          verbose_name_plural = _("Brands")

     def __str__(self):
          return self.BRDName

class Variant(models.Model):
     VARName = models.CharField(verbose_name=_("Name"), max_length=50)
     VARDesc = models.TextField(verbose_name=_("Description"),blank=True, null=True)
    

     class Meta:
          verbose_name = _("Variant")
          verbose_name_plural = _("Variants")

     def __str__(self):
          return self.VARName

