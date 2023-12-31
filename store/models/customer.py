from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    password = models.CharField(max_length=100)
    # address = models.CharField(max_length=500,default=None)
    
     #to save the data
    def register(self):
        self.save()

    @property
    def get_name(self):
        return self.first_name+" "+self.last_name
    @property
    def get_id(self):
        return self.id
 
    def __str__(self):
        return self.first_name


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email= email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False