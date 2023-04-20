from django.urls import path
from .views import (CarViewSet, 
    KonfiguratorViewSet,
    Konfiguratorget,
    CarViewdelete,
    )

urlpatterns = [
    path('car/', CarViewSet.as_view()),
    path('car/<int:pk>/', CarViewSet.as_view()),
    path('konfigurator/', KonfiguratorViewSet.as_view()),
    path('konfigurator/<int:pk>/', Konfiguratorget.as_view()),
    path('car/delete/<int:pk>/', CarViewdelete.as_view()),
]