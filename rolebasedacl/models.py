from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Role(models.Model):
    """
    A role which is defined by a django project user
    """
    name = models.CharField(max_length=255, unique=True)
    desc = models.TextField(blank=True)

    def __unicode__(self):
        return '%s' % self.name

class Operation(models.Model):
    """
    An action which is defined by a django project user
    """
    name = models.CharField(max_length=255, unique=True)
    desc = models.TextField(blank=True)

    def __unicode__(self):
        return '%s' % self.name

class Perm(models.Model):
    """
    A permission can be given to
    * 1 or many operations
    * 1 or many objects
    Many permissions can be given to many roles
    """
    owner_ct = models.ForeignKey(ContentType, related_name='permission_owner')
    owner_id = models.IntegerField()
    owner = generic.GenericForeignKey('owner_ct', 'owner_id')
    
    object_ct = models.ForeignKey(ContentType, related_name='permission_object')
    object_id = models.IntegerField()
    object = generic.GenericForeignKey('object_ct', 'object_id')
    
    roles = models.ManyToManyField(Role, related_name='permissions')
    operation = models.ForeignKey(Operation) 

    class Meta:
        unique_together = ('owner_ct', 'owner_id', 'object_ct', 'object_id', 'operation')

    def __unicode__(self):
        return '%s | %s | %s' % (self.owner, self.object. self.operation)
