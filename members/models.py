from django.db import models
class main_model(models.Model):
    user=models.CharField(default="patients",max_length=50)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    profile_pit=models.ImageField(upload_to='profile_pic',blank=True)
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    Address=models.TextField(max_length=200)
