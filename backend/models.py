# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
