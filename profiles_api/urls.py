from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset', views.helloViewSet, base_name='hello-viewset')


urlpatterns = [
    path('hello-view', views.helloAPIView.as_view()),
    path('', include(router.urls))
]
