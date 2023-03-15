from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Item(models.Model):
     category=models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
     name=models.CharField(max_length=225)
     description=models.TextField(blank=True,null=True)
     price=models.FloatField()
     image=models.ImageField(upload_to='item_images',blank=True,null=True)
     is_sold=models.BooleanField()
     created_at=models.DateField(auto_now_add=True)
     created_by=models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)

