from django.db import models
from django.contrib.auth.models import User

class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_picture = models.ImageField(upload_to='id_pictures/')
    face_picture = models.ImageField(upload_to='face_pictures/')
    # Add any other fields you need for the seller

class Store(models.Model):
    owner = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    store_picture = models.ImageField(upload_to='store_pictures/')

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    NEW = 'NEW'
    USED = 'USED'
    REFURBISHED = 'REFURBISHED'
    CONDITION_CHOICES = [
        (NEW, 'New'),
        (USED, 'Used'),
        (REFURBISHED, 'Refurbished'),
    ]
    AVAILABLE = 'Available'
    SOLD = 'Sold'

    STATUS_CHOICES = [
        (AVAILABLE, 'Available'),
        (SOLD, 'Sold'),
    ]
    item_id = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=11, choices=CONDITION_CHOICES)
    brand = models.CharField(max_length=255, blank=True)
    model_number = models.CharField(max_length=255, blank=True)
    stock = models.IntegerField()
    seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
    date_listed = models.DateTimeField(auto_now_add=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    tags = models.TextField(blank=True)
    view_count = models.IntegerField(default=0)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=AVAILABLE)

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.title}"



class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

class PurchaseHistory(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    purchase_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.buyer.username} - {self.product.title}"


class SalesList(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    item_status = models.CharField(max_length=100)
    date_of_sale = models.DateTimeField(auto_now_add=True)

class Payment(models.Model):
    transaction_id = models.CharField(max_length=255, unique=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)
    payment_details = models.TextField()
    order_reference = models.ForeignKey(SalesList, on_delete=models.SET_NULL, null=True)
    receipt_url = models.URLField(max_length=255, blank=True)

    def __str__(self):
        return self.transaction_id

class SellerRating(models.Model):
    seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
    rater = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5 scale
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('seller', 'rater')  # Each user rates a seller only once

    def __str__(self):
        return f"{self.rating} for {self.seller.user.username} by {self.rater.username}"

class SellerReview(models.Model):
    seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.seller.user.username} by {self.reviewer.username}"
