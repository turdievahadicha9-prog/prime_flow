from django.db import models

class Flower(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='flowers/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    flower = models.ForeignKey(
        Flower,
        on_delete=models.CASCADE
    )


    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    receiver_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.customer_name} -> {self.flower.name}'