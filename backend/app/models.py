from django.db import models
from djongo.models import FloatField, DecimalField

class CouriersTest(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    autoassignmentenabled = models.IntegerField(db_column='autoAssignmentEnabled', blank=True, null=True)  # Field name made lowercase.
    numberoforders = models.IntegerField(db_column='numberOfOrders', blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(blank=True, null=True)
    transport = models.TextField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    mcd = models.IntegerField(blank=True, null=True)
    mcc = models.IntegerField(blank=True, null=True)
    checkedin = models.IntegerField(db_column='checkedIn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'couriers_test'
