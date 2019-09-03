from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from api import views

# Auto-generate schema from API
schema_view = get_schema_view(title='Specimen Observer API')

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'batch', views.UploadBatchesViewSet)
router.register(r'observation', views.ObservationsViewSet)
router.register(r'image', views.ImagesViewSet)

# The API URLS are now automatically determined by the router
urlpatterns = [
    path('schema/', schema_view),
    path('', include(router.urls)),
]