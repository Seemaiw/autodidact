from django.urls import include, path
from rest_framework.routers import DefaultRouter

from post.views import PostViewSet, CategoryViewSet

router = DefaultRouter()
router.register('api/post', PostViewSet, base_name='post')
router.register('api/category',  CategoryViewSet, base_name='category')

urlpatterns = [
    path('', include(router.urls)),
]

