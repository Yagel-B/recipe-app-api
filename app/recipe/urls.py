from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# YBD: This auto register all default routers like: get_all,
# get_by_id (for example /api/recipe/tags/1/)
router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
