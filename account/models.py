from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    category = models.CharField(unique=True, max_length=50, null=True, blank=True)

    def __str__(self):
        return self.category
    


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return self.subcategory



class Professional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sub_category = models.ManyToManyField(SubCategory, blank=True)
    business_name = models.CharField(max_length=100, null=True, blank=False)
    phone_no = models.CharField(unique=True, max_length=13, null=True)
    job_completed = models.IntegerField(default=0)
    address = models.TextField(default=" ", null=True, blank=True)
    service_charge = models.CharField(null=True, blank=True, max_length=10)
    logo = models.ImageField(upload_to="professional_photo", null=True)
    joining_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username 



class UploadImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="all_images", null=True)
    

    def __str__(self):
        return self.user.username
    


CHOICES = (
    ('User-Verified', 'User-Verified'),
    ('Non-Verified', 'Non-Verified')
)

class RequestVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    request_image = models.ImageField(upload_to="request_verification_images", null=True)
    status = models.CharField(max_length=20, null=True, choices=CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username



class Package(models.Model):
    user = models.ForeignKey(User, related_name='packages', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=50, null=True, blank=True)
    about = models.TextField(null=True)
    time = models.DateTimeField(auto_now=True)
    package_image = models.ImageField(upload_to="package_images", null=True)
    cost = models.FloatField(default=0.0)
    cost_factor = models.FloatField(default=1.0)


    def __str__(self):
        return self.user.username + " ----> " + self.package_name