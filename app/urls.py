from django.urls import path
from .views import (
    CarViewSet, 
    KonfiguratorViewSet,
    Konfiguratorget,
    CarViewdelete,
    Carget,
    Konfiguratordelete,
    DileryViewSet,
    Dilerydelete,
    Extiyot_qisimlarView,
    Extiyot_qisimlardelete,
    Sub_extiyotqisimlarView,
    Sub_extiyot_delet
    )

urlpatterns = [
    path('car/', CarViewSet.as_view()),
    path('car/delete/<int:pk>/', CarViewdelete.as_view()),
    path('car/get/<int:pk>/', Carget.as_view()),

    path('konfigurator/', KonfiguratorViewSet.as_view()),
    path('konfiguratorget/<int:pk>/', Konfiguratorget.as_view()),
    path('konfigurator/delete/<int:pk>/', Konfiguratordelete.as_view()),

    path('dilery/', DileryViewSet.as_view()),
    path('dilery/delete/<int:pk>/', Dilerydelete.as_view()),

    path('extiyot_qisimlar/', Extiyot_qisimlarView.as_view()),
    path('extiyotqisimlar_delet/<int:pk>/', Extiyot_qisimlardelete.as_view()),
    path('sub_extiyotqisimlar/', Sub_extiyotqisimlarView.as_view()),
    path("sub_extiyotqisimlar/<int:id>/", Sub_extiyotqisimlarView.as_view(), name="sub_extiyotqisimlar"),
    path("sub_extiyot_delet/<int:pk>/", Sub_extiyot_delet.as_view()),
]