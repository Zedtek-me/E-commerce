from django.urls import path
from . import views, api_views
urlpatterns=[
    path('', views.index, name='home' ),
    # api urls below
    path('vendor/', api_views.get_vendor, name='vendors' ),
    path('buyer/', api_views.get_buyer, name='buyers' ),
    path('product/', api_views.get_product, name='products' ),

    # urls to template views
    path('login/', views.login, name='login' ),
    path('signup/', views.signup, name='signup' ),
]