from django.db import models

# Create your models here.

class Product(models.Model): 
    title       = models.CharField(max_length=120) # @max_length param is required
    description = models.TextField(blank= True,null=True)
    price       = models.DecimalField(max_digits=10000,decimal_places=2)
    summary     = models.TextField(blank = True,null= False)#@blank - True/False, if it is true it will
                                                            #render as it is not required (ie not bold)
                                                            #@null - is a null value valid for this field
    
    featured    = models.BooleanField() # if we add a new model without setting either a null or default 
                                        # all previous instances of the database which do 
                                        # not have this new field will result in an error
