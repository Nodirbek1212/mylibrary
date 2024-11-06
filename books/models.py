import os
from django.db import models
from ckeditor import fields

class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images')
    description = models.TextField()
    about = fields.RichTextField()
    uzbek_literature = models.BooleanField(default=True)
    start_date = models.DateField()
    finish_date = models.DateField(blank=True, null=True)
    slug = models.SlugField(default="")

    def __str__(self):
        return self.title
            

    def save(self, *args, **kwargs):
        # If an object with an image already exists, delete the old image
        if self.pk:
            try:
                old_img = Book.objects.get(pk=self.pk).img
                if old_img and old_img != self.img:
                    if os.path.isfile(old_img.path):  # Check if the file exists
                        os.remove(old_img.path)  # Remove the old image from storage
            except Book.DoesNotExist:
                pass  # If the object is new, no action needed

        # Save the new image
        super().save(*args, **kwargs)
