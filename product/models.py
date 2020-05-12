from django.db import models
from django.utils import timezone 
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify 
from django.urls import reverse 

# from django.db.models.signals import post_save
# Create your models here.
""" عشان ال relation متعملش مشاكل ابقي حط  ' ' و اسم ال  model """
class Category(models.Model):
	CATName= models.CharField(verbose_name=_("Category Name"), max_length=80)
	CATParent  = models.ForeignKey("self",limit_choices_to={'CATParent__isnull':True} ,verbose_name=_("Parent Category"), on_delete=models.CASCADE, blank=True,null=True)
	CATDesc = models.TextField(verbose_name=_("Description"))
	CATImg  = models.ImageField(verbose_name=_("Image"), upload_to='category/%Y/%m/%d/')

    
	class Meta:
		verbose_name = _("Category")
		verbose_name_plural = _("Categories")

	def __str__(self):
		return self.CATName


class Product(models.Model):
     PRDName = models.CharField(max_length=100, verbose_name=_("Product Name"))
     PRDCategory = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.CASCADE, blank=True, null=True)
     PRDBrand = models.ForeignKey("settings.Brand", verbose_name=_("Brand"), on_delete=models.CASCADE, blank=True, null=True)
     PRDDesc = models.TextField(verbose_name=_("Description"))
     PRDPrice = models.DecimalField( max_digits=5, decimal_places=2,verbose_name=_("Price"))
     PRDDiscountPrice = models.DecimalField( max_digits=5, decimal_places=2,verbose_name=_("Discount Price"))
     PRDCost = models.DecimalField( max_digits=5, decimal_places=2,verbose_name=_("Cost"))
     PRDCreated = models.DateTimeField(default=timezone.now,verbose_name=_("Created at"))
     PRDImage_1 = models.ImageField(verbose_name=_("Product Main Image"), upload_to='products/%Y/%m/%d/')
     PRDImage_2 = models.ImageField(verbose_name=_("Product Image 2"), upload_to='products/%Y/%m/%d/',blank=True, null=True)
     PRDImage_3 = models.ImageField(verbose_name=_("Product Image 3"), upload_to='products/%Y/%m/%d/',blank=True, null=True)
     PRDImage_4 = models.ImageField(verbose_name=_("Product Image 4"), upload_to='products/%Y/%m/%d/',blank=True, null=True)
     PRDSlug = models.SlugField(verbose_name=_("Slug"), blank=True, null=True)
     PRDISNew = models.BooleanField(default=True, verbose_name=_("New Product ?"))
     PRDISBestseller = models.BooleanField(default=False, verbose_name=_("BestSeller"))


     class Meta:
          verbose_name = _("Product")
          verbose_name_plural = _("Products")
		
     def __str__(self):
	     return self.PRDName

     def save(self, *args, **kwargs):
          if not self.PRDSlug:
               self.PRDSlug = slugify(self.PRDName)
          super(Product, self).save(*args, **kwargs) # Call the real save() method
     
     def get_absolute_url(self):    
          return reverse('product_detail', kwargs={'slug': self.PRDSlug})


class Product_Alternative(models.Model):
     PALNProduct = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE, related_name='main_product')
     PALNAlternative = models.ManyToManyField(Product, verbose_name=_("Product_Alternative"),related_name='alternative_products')
     class Meta:
          verbose_name = _("Product_Alternative")
          verbose_name_plural = _("Product Alternative")

     def __str__(self):
          return self.PALNProduct.PRDName

class Product_Accessoris(models.Model):
     PACCProduct = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE, related_name='mainAccessoris_product')
     PACCAlternative = models.ManyToManyField(Product, verbose_name=_("Product Accessoris"),related_name='product_accessoris')
    

     class Meta:
          verbose_name = _("Product_Accessoris")
          verbose_name_plural = _("Product Accessories")

     def __str__(self):
          return str(self.PACCProduct)
