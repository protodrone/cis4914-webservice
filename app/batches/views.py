from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.conf import settings
from api.models import UploadBatches
from api.models import Observations
from api.models import Images
from .batch_utilities import batchImageDepth
import csv

class WelcomePage(TemplateView):
    template_name = 'batches/welcomepage.html'

class BatchesList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'is_download_authorized'
    model = UploadBatches
    context_object_name = "batches"
    template_name = 'batches/batches.html'

class BatchDetailList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'is_download_authorized'
    template_name = "batches/batchdetail.html"
    context_object_name = "observations"

    def get_queryset(self):
        self.batch = get_object_or_404(UploadBatches, pk=self.kwargs['batchId'])
        return Observations.objects.filter(upload_batch=self.kwargs['batchId'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['batch'] = self.batch
        return context

class ObservationDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'is_download_authorized'
    model = Observations
    context_object_name = "observation"
    template_name = 'batches/observationdetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Images.objects.filter(observation=self.kwargs['pk'])
        return context

@login_required
@permission_required('is_download_authorized')
def DeleteBatch(request,batchId):
    batch = get_object_or_404(UploadBatches, pk=batchId)
    batch.delete()
    return redirect('batches')

@login_required
@permission_required('is_download_authorized')
def downloadBatchCSV(request,batchId):
    batch = get_object_or_404(UploadBatches, pk=batchId)
    observations = Observations.objects.filter(upload_batch=batch.id)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(batch.batch_name)
    print(batch.batch_name)
    writer = csv.writer(response)
    column_headers = ['observation_name',
                    'lattitude',
                    'longitude',
                    'gps_datum',
                    'Text1',
                    'Text2',
                    'Text3',
                    'Int1',
                    'Int2',
                    'Int3',
                    'notes']
    image_depth = batchImageDepth(batchId)
    for i in range(0,image_depth):
        column_headers.append('image{}'.format(i+1))
    writer.writerow(column_headers)
    for obs in observations:
        row_data = [
            obs.observation_name,
            obs.lattitude,
            obs.longitude,
            obs.gps_datum,
            obs.Text1,
            obs.Text2,
            obs.Text3,
            obs.Int1,
            obs.Int2,
            obs.Int3,
            obs.notes
        ]
        if image_depth > 0:
            images = Images.objects.filter(observation=obs.id)
            for image in images:
                row_data.append(request.scheme+'://'+request.headers['Host']+settings.MEDIA_URL+str(image.image))    
        writer.writerow(row_data)
    return response

