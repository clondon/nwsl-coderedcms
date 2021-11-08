from django.db import models


class Customer(models.Model):
    """ Customer models """
    customer_name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=200)

    def __str__(self):
        return self.customer_name + ' ' + self.customer_name



    
