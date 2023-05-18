from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class SocietyList(models.Model):
    societyName = models.CharField(max_length=122)
    regno = models.CharField(max_length=122)
    address = models.TextField()
    date_add_society = models.DateField()

    def __str__(self):
        return self.societyName
    