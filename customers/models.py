from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse


class Person(models.Model):
    name = models.CharField("Name", max_length=255)
    cpf = models.CharField("CPF", max_length=14,
                           validators=[MinLengthValidator(11)], unique=True)
    email = models.EmailField("Email", max_length=254, unique=True)
    phone = models.CharField("Phone number", max_length=12)
    address1 = models.CharField("Address line 1", max_length=1024)
    address2 = models.CharField("Address line 2", max_length=1024)
    postal_code = models.CharField("Postal code", max_length=12)
    city = models.CharField("City", max_length=1024)
    country = models.CharField("Country", max_length=3)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ("-created_on", )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("customers:detail", kwargs={"pk": self.pk})
