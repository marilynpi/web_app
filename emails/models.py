from django.db import models

class ContactForm(models.Model):

    form_name = models.CharField(max_length=100)
    name_field = models.CharField(max_length=30, null=True)
    email_field = models.EmailField(max_length=254, null=True)
    message_field = models.CharField(max_length=100, null=True)
    subject_field = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.form_name

    class Meta:
        verbose_name = "Contact Form"
