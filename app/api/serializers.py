from rest_framework import serializers
from api.models import UploadBatches, Observations, Images
from django.contrib.auth.models import User

class UploadBatchesSerializer(serializers.ModelSerializer):
    """
    Upload Batches
    """
    class Meta:
        model = UploadBatches
        fields = ('batch_name')

class ObservationsSerializer(serializers.ModelSerializer):
    """
    Specimen Observations
    """
    class Meta:
        model = Observations
        fields = ('upload_batch',
                  'observation_name',
                  'lattitude',
                  'longitude',
                  'gps_datum',
                  'Text1',
                  'Text2',
                  'Text3',
                  'Int1',
                  'Int2',
                  'Int3',
                  'notes')

class ImagesSerializer(serializers.ModelSerializer):
    """
    Observation Images
    """
    class Meta:
        model = Images
        fields = ('observation',
                  'image_name')
