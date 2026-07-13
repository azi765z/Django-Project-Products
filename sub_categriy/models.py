from django.db import models
from categriy.models import CategoriyModel
# Create your models here.

class SubCategoryModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="subcategories/", blank=True, null=True)
    category = models.ForeignKey(CategoriyModel, on_delete=models.CASCADE, related_name='subcategories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
