# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CommentStar(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=1000, blank=True, null=True)
    star = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment_star'
