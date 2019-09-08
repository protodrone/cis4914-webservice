from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from api import views

# Auto-generate schema from API
schema_view = get_schema_view(title='Specimen Observer API')

# Create a router and register our viewsets
# Trailing slash dragon. https://www.django-rest-framework.org/api-guide/routers/#defaultrouter
router = DefaultRouter(trailing_slash=False) 
router.register(r'batch', views.UploadBatchesViewSet)
router.register(r'observation', views.ObservationsViewSet)
router.register(r'image', views.ImagesViewSet)

# The API URLS are now automatically determined by the router
urlpatterns = [
    path('schema/', schema_view),
    path('', include(router.urls)),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]