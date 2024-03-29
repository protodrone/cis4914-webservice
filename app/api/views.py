from django.shortcuts import render
from api.models import UploadBatches, Observations, Images
from api.serializers import UploadBatchesSerializer, ObservationsSerializer, ImagesSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from api.permissions import IsAPIAuthorized
from django.http import Http404
import os
from django.conf import settings

class UploadBatchesViewSet(viewsets.ModelViewSet):
    """
    viewset.ModelViewsets automatically provides `list`, `create`,
    `retrieve`, `update`, and `destroy` actions.

    Additional actions may be provided with the @action decorator.
    """
    queryset = UploadBatches.objects.all()
    serializer_class = UploadBatchesSerializer
    permission_classes = [IsAPIAuthorized]

class ObservationsViewSet(viewsets.ModelViewSet):
    """
    Specimen Observations
    """
    queryset = Observations.objects.all()
    serializer_class = ObservationsSerializer
    permission_classes = [IsAPIAuthorized]

class ImagesViewSet(viewsets.ModelViewSet):
    """
    Observation Images
    """
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = [IsAPIAuthorized]
    