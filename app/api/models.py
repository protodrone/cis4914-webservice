from django.db import models
import datetime

# Base model to include audit trail.
class BaseModel(models.Model):
    created_by = models.CharField(max_length=15)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=15)
    class Meta:
        abstract = True

class UploadBatches(BaseModel):
    batch_name = models.CharField(max_length=50)
    def __str__(self):
        return self.batch_name
    class Meta:
        verbose_name = "Collection Batch"
        verbose_name_plural = "Collection Batches"

class Images(BaseModel):
    image_name = models.CharField(max_length=50)
    # BLOB or file path upload placeholder
    def __str__(self):
        return self.image_name
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

class Observations(BaseModel):
    observation_name = models.CharField(max_length=20)
    lattitude = models.DecimalField()
    longitude = models.DecimalField()
    gps_datum = models.CharField(max_length=10)
    Text1 = models.CharField(max_length=50,null=True)
    Text2 = models.CharField(max_length=50,null=True)
    Text3 = models.CharField(max_length=50,null=True)
    Int1 = models.IntegerField(null=True)
    Int2 = models.IntegerField(null=True)
    Int3 = models.IntegerField(null=True)
    notes = models.TextField(null=True)
