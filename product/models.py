
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class UserA(AbstractBaseUser):
    uname = models.CharField(max_length=20,null=True)
    password = models.CharField(max_length=10,null=True)
    
    USERNAME_FIELD='uname'
    
    def __str__(self):
        return self.uname
    

class Product(models.Model):
    AVAILABLE = 'available'
    OUT_OF_STOCK = 'out_of_stock'

    STATUS_CHOICES = [
        (AVAILABLE, 'Available'),  
        (OUT_OF_STOCK, 'Out of Stock'),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=AVAILABLE  
    )

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.stock <= 0:
            self.status = self.OUT_OF_STOCK
        else:
            self.status = self.AVAILABLE
        super(Product, self).save(*args, **kwargs)  



    

class Order(models.Model):
    user=models.ForeignKey(UserA,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price=models.DecimalField(max_digits=10, decimal_places=2)
    discount=models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=0, 
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    final_price=models.DecimalField(max_digits=10,decimal_places=2,editable=False)
    
    
    def save(self, *args, **kwargs):
        """Override save method to automatically calculate the final price."""
        self.price = self.product.price * self.quantity
        discount_amount = self.price * (self.discount / 100)
        self.final_price = self.price - discount_amount
        super().save(*args, **kwargs)

        if self.quantity <= self.product.stock:  
            self.product.stock -= self.quantity
            self.product.save()  
        
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"Order for {self.product.name} with quantity {self.quantity}"