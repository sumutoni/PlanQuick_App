from planquick import settings
from django.db import models
User = settings.AUTH_USER_MODEL
#from django.contrib.auth.models import User

class Transactions(models.Model):
    created_at = models.DateField()
    ref_id = models.CharField(max_length=50, unique=True)
    trn_type = models.CharField(max_length=50)
    amount = models.IntegerField(null=True)
    trn_date = models.DateField(null=True)
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.owner