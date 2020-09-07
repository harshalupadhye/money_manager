from django.db import models

# Create your models here.
class wallet(models.Model):
    wallet_id = models.IntegerField()
    user_name = models.CharField(max_length=20)
    money = models.IntegerField()
    def __str__(self):
        return self.user_name


