from django.db import models
from django.db.models.fields.json import JSONField

# Create your models here.

class Tool(models.Model):
  label = models.CharField(max_length=1024, null=True, blank=True)
  description = models.TextField(null=True, blank=True)

class ToolInput(models.Model):
  tool = models.ForeignKey(
    Tool,
    related_name="inputs",
    on_delete= models.CASCADE
  )
  name = models.CharField(
    max_length=1024,
    null=True,
    blank=True
  )
  value = JSONField(null=True, blank=True)