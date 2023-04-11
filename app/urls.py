from django.urls import path
from .views import CarViewSet, KonfiguratorViewSet

urlpatterns = [
    path('car/', CarViewSet.as_view()),
    path('car/<int:pk>/', CarViewSet.as_view()),
    path('konfigurator/', KonfiguratorViewSet.as_view()),
    path('konfigurator/<int:pk>/', KonfiguratorViewSet.as_view()),
]