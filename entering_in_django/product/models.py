from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, primary_key=True)  # латинский алфовит, нижний регистр, пробелы заполняются на -/_, не допускает к названию спец символов
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self) -> str:
        return self.title