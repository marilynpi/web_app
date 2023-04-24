from django.db import models

class ContactForm(models.Model):

    form_name = models.CharField(max_length=100)
    name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=254, null=True)
    message = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    last_update = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.form_name

    class Meta:
        verbose_name = "Contact Form"

class Billing(ContactForm):

    lastname = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.form_name
    class Meta:
        verbose_name = "Billing Data"
