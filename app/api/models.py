from django.db import models
from django.conf import settings
import datetime, uuid
from crum import get_current_user
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Base model to include audit trail.
class BaseModel(models.Model):
    created_by = models.CharField(max_length=15)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=15)
    modified_timestamp = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        abstract = True
    def save(self, *args, **kwargs):
        u = get_current_user()
        if self._state.adding:
            self.created_by = u.username
        self.modified_by = u.username
        self.modified_timestamp = datetime.datetime.now()
        super().save(*args, **kwargs)

class UploadBatches(BaseModel):
    batch_name = models.CharField(max_length=50)
    def __str__(self):
        return self.batch_name
    class Meta:
        verbose_name = "Collection Batch"
        verbose_name_plural = "Collection Batches"

class Observations(BaseModel):
    upload_batch = models.ForeignKey(UploadBatches,on_delete=models.CASCADE)
    observation_name = models.CharField(max_length=20)
    lattitude = models.DecimalField(max_digits=25,decimal_places=15,null=True)
    longitude = models.DecimalField(max_digits=25,decimal_places=15,null=True)
    gps_datum = models.CharField(max_length=10,null=True)
    Text1 = models.CharField(max_length=50,null=True)
    Text2 = models.CharField(max_length=50,null=True)
    Text3 = models.CharField(max_length=50,null=True)
    Int1 = models.IntegerField(null=True)
    Int2 = models.IntegerField(null=True)
    Int3 = models.IntegerField(null=True)
    notes = models.TextField(null=True)
    def __str__(self):
        return self.observation_name
    class Meta:
        verbose_name = "Observation"
        verbose_name_plural = "Observations"

class Images(BaseModel):
    observation = models.ForeignKey(Observations,on_delete=models.CASCADE)
    image_name = models.CharField(max_length=50)
    image = models.ImageField()
    def __str__(self):
        return self.image_name
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
    def save(self, *args, **kwargs): # Override save to rename file MEDIA_ROOT/BatchID/UUID
        if self._state.adding: # detect if first save
            obs = Observations.objects.get(pk=self.observation.id) # get observation object
            batch = obs.upload_batch.id # get batchID from observation
            self.image.name = str(batch) + "/" + str(uuid.uuid4()) + self.image.name[self.image.name.rfind('.'):]
        super().save(*args, **kwargs)

@receiver(post_delete, sender=Images)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)
