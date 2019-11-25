from django.urls import path, include
from batches import views

urlpatterns = [
    path('', views.BatchesList.as_view(), name='batches'),
    path('<int:batchId>', views.BatchDetailList.as_view(), name='batches'),
    path('observation/<int:pk>/', views.ObservationDetail.as_view(), name="observation_detail"),
    path('batchcsv/<int:batchId>/', views.downloadBatchCSV, name="downloadCSV"),
    path('deletebatch/<int:batchId>/', views.DeleteBatch, name="deletebatch"),
]