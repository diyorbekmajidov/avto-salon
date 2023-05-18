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
    Sub_extiyot_delet,
    Sub_QisimlarUpdate,
    Usercreateviews,
    Userlogoutviews,
    Userloginviews,
    CartView,
    Cartdelete,
    Cart_extiyotqisimlarView,
    Cart_extiyotqisimlardelete,
    LikeCarViews,
    LikeCardelete,
    All_lekicar,
    LikeUpdate,
    )

urlpatterns = [
    path('car/', CarViewSet.as_view()),
    path('car/delete/<int:pk>/', CarViewdelete.as_view()),
    path('car/get/<int:pk>/', Carget.as_view()),
    path('car/<int:pk>/', CarViewSet.as_view(), name="car"),

    path('konfigurator/', KonfiguratorViewSet.as_view()),
    path('konfigurator/<int:pk>/', KonfiguratorViewSet.as_view(), name="konfigurator update"),
    path('konfiguratorget/<int:pk>/', Konfiguratorget.as_view()),
    path('konfigurator/delete/<int:pk>/', Konfiguratordelete.as_view()),

    path('dilery/', DileryViewSet.as_view()),
    path('dilery/delete/<int:pk>/', Dilerydelete.as_view()),

    path('extiyot_qisimlar/', Extiyot_qisimlarView.as_view()),
    path('extiyotqisimlar_delet/<int:pk>/', Extiyot_qisimlardelete.as_view()),

    path('sub_extiyotqisimlar/', Sub_extiyotqisimlarView.as_view()),
    path("sub_extiyotqisimlar/<int:pk>/", Sub_extiyotqisimlarView.as_view(), name="sub_extiyotqisimlar"),
    path("sub_update/<int:pk>/", Sub_QisimlarUpdate.as_view(), name="sub_extiyotqisimlar update" ),
    path("sub_extiyot_delet/<int:pk>/", Sub_extiyot_delet.as_view()),

    path("usercreate/", Usercreateviews.as_view()),
    path("userlogout/", Userlogoutviews.as_view()),
    path("userlogin/", Userloginviews.as_view()),

    path("cartcar/", CartView.as_view()),
    path("cartcar/<int:pk>/", CartView.as_view(), name="cartcar update"),
    path("cartcardelete/<int:pk>/", Cartdelete.as_view()),

    path("cart_extiyotqisimlar/", Cart_extiyotqisimlarView.as_view()),
    path("cart_extiyotqisimlar/<int:pk>/", Cart_extiyotqisimlarView.as_view(), name="cart_extiyotqisimlar update"),
    path("cart_extiyotqisimlardelete/<int:pk>/", Cart_extiyotqisimlardelete.as_view()),

    path("likecar/", LikeCarViews.as_view()),
    path("likecardelete/<int:pk>/", LikeCardelete.as_view()),
    path("all_lekicar/", All_lekicar.as_view()),
    path("likeupdate/<int:pk>/", LikeUpdate.as_view()),
    
]