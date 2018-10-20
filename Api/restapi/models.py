# Create your models here.
from django.db import models

class UserDetail(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=20)
    companyName =  models.CharField(max_length=100, blank=True, default='')
    city       = models.CharField(max_length=20)
    state      = models.CharField(max_length=20)
    zip        = models.IntegerField()
    email      = models.EmailField(max_length=70,blank=True)
    web        = models.URLField()
    age        = models.IntegerField() 

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return '%s %s %s %s %s %d %s %s %d' % (self.first_name,self.last_name,self.companyName,
        self.city,self.state,self.zip,self.email,self.web,self.age)