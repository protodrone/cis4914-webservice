from django.urls import path, include
from batches import views

urlpatterns = [
    path('', views.BatchesList.as_view(), name='batches'),
    path('<int:batchId>', views.BatchDetailList.as_view(), name='batches'),
    path('observation/<int:pk>/', views.ObservationDetail.as_view(), name="observation_detail"),
]