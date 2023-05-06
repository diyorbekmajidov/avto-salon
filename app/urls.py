from django.urls import path
from .views import (CarViewSet, 
    KonfiguratorViewSet,
    Konfiguratorget,
    CarViewdelete,
    Konfiguratordelete,
    DileryViewSet,
    Dilerydelete,
    )

urlpatterns = [
    path('car/', CarViewSet.as_view()),
    path('car/<int:pk>/', CarViewSet.as_view()),
    path('konfigurator/', KonfiguratorViewSet.as_view()),
    path('konfigurator/<int:pk>/', Konfiguratorget.as_view()),
    path('car/delete/<int:pk>/', CarViewdelete.as_view()),
    path('konfigurator/delete/<int:pk>/', Konfiguratordelete.as_view()),
    path('dilery/', DileryViewSet.as_view()),
    path('dilery/delete/<int:pk>/', Dilerydelete.as_view()),
]