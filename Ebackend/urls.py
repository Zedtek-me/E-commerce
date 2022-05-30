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
    path('logout/', views.logout_user, name='logout' ),
    path('signup/', views.signup, name='signup' ),
    path('profile/', views.profile, name='profile' ),
    path('checkout/', views.check_out, name='checkout'),
    path('payment/', views.payment_method, name= 'payment'),
    path('remove-prod/', views.remove_prod, name= 'remove-prod'),
    path('edit-prod/', views.edit_product, name= 'edit-prod'),
    path('add_to_cart/', views.add_to_cart, name= 'add_to_cart'),
    path('remove_from_cart/', views.remove_from_cart, name= 'remove_from_cart'),
    path('search/', views.search, name= 'search'),
    path('update-acc/', views.update_account, name="update account")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)