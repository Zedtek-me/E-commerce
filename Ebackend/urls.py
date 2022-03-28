from unicodedata import name
from django.urls import path
from . import views, api_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    # api urls below
    path('vendor/', api_views.get_vendor, name='vendors' ),
    path('buyer/', api_views.get_buyer, name='buyers' ),
    path('product/', api_views.get_product, name='products' ),

    # urls to template views
    path('', views.index, name='home' ),
    path('login/', views.login_user, name='login' ),
    path('logout', views.logout_user, name='logout' ),
    path('signup/', views.signup, name='signup' ),
    path('profile/', views.profile, name='profile' ),
    path('checkout/', views.check_out, name='checkout'),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)