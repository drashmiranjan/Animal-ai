from django.db import models

# Create your models here.
class AnimalModel(models.Model):
    image = models.ImageField(upload_to='animal_images/')
    uploaded_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"image uploaded at {self.uploaded_at}"