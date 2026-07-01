from django.urls import path, re_path
from shop import views

urlpatterns = [
    path('', views.shopHome, name="shophome"),
    path('search/<str:shop_id>', views.searchShop, name="searchShop"),

    # these re_path are used to define the parameter info the we are getting 
    # regex is used in this to define that after shop/ the year must contains 4 digis
    re_path(r'^shop/(?P<year>[0-9]{4})$', views.shopByOpeningYear, name="year"),

    # Multiple arguments handlings...
    path('info/<int:shop_id>/<str:shop_name>', views.shopInformations, name="shopInformations")
]