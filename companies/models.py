from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(unique=True, max_length=200)
    gst = models.CharField(unique=True, max_length=200)

class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    product = models.CharField(max_length=200, unique=True)
    cost = models.DecimalField(null=False, decimal_places=2, max_digits=20)
    # could also add datefields for when the product was launched and such

# unable to find a solution which aggregates the total and saves it
class Invoice(models.Model):
    total = models.DecimalField(decimal_places=2, max_digits=20)
    generated_on = models.DateField(auto_now_add= True)
    pass

class Order(models.Model):
    invoice_id = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    # kept many to many as if in future we would like to see orders by a company, we could get it
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.DecimalField(decimal_places=2, max_digits=20)

    def save(self, *args, **kwargs):
        self.total = self.quantity * self.product.cost
        super(Order, self).save(*args, **kwargs)