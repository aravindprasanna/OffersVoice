# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#from django.db import models
from djongo import models
from django.contrib.postgres.fields import JSONField
from djongo.models.fields import ObjectIdField

class Offers(models.Model):

    field_id = ObjectIdField(db_column='_id')  # Field renamed because it started with '_'.
    offer_id = models.CharField(unique=True, max_length=6)
    offer_url = models.CharField(max_length=73)
    offer_brief = models.CharField(max_length=181)
    offer_description = models.TextField()
    offer_details = models.TextField()
    offer_period = models.CharField(max_length=44)
    offer_channel = models.CharField(max_length=42)

    objects = models.DjongoManager()

    class Meta:
        db_table = 'Offers'


class OffersMapping(models.Model):
    field_id = ObjectIdField(db_column='_id')  # Field renamed because it started with '_'.
    offer_type = models.CharField(max_length=6)
    offer_card = models.CharField(max_length=9)
    offer_activity = models.CharField(max_length=5)
    offer_list = JSONField()

    objects = models.DjongoManager()

    class Meta:
        db_table = 'Offers_Mapping'
