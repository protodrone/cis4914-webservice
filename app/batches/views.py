from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from api.models import UploadBatches
from api.models import Observations

class BatchesList(ListView):
    #permission_required = 'flowsheets.can_view_companies'
    model = UploadBatches
    context_object_name = "batches"
    template_name = 'batches/batches.html'

class BatchDetailList(ListView):
    template_name = "batches/batchdetail.html"
    context_object_name = "observations"

    def get_queryset(self):
        batch = get_object_or_404(UploadBatches, pk=self.kwargs['batchId'])
        self.batch_name = batch.batch_name
        return Observations.objects.filter(upload_batch=self.kwargs['batchId'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['batch_name'] = self.batch_name
        return context

class ObservationDetail(DetailView):
    model = Observations
    context_object_name = "observation"
    template_name = 'batches/observationdetail.html'
