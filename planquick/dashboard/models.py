from planquick import settings
from django.db import models
User = settings.AUTH_USER_MODEL
#from django.contrib.auth.models import User

class Transactions(models.Model):
    created_at = models.DateField(null=True)
    ref_id = models.CharField(max_length=50)
    trn_type = models.CharField(max_length=50)
    amount = models.IntegerField(null=True)
    trn_date = models.DateField(null=True)
    owner = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % self.owner
    

