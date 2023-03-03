from django.db import models

# Create your models here.
class Fund(models.Model):
    name = models.CharField(max_length=200, blank=False)
    strategy = models.CharField(max_length=200, blank=False)
    aum = models.IntegerField('AUM (USD)', null=True, blank=True)
    inception_date = models.DateTimeField('Inception Date', null=True,  blank=True)

    def __str__(self):
        return self.name