from django.urls import include, path
from rest_framework.routers import DefaultRouter

from post.views import PostViewSet, CategoryListCreateAPIView

router = DefaultRouter()
router.register('api/post', PostViewSet, base_name='post')

urlpatterns = [
    path('', include(router.urls)),
    path('api/category',  CategoryListCreateAPIView.as_view(), name='category' )
]