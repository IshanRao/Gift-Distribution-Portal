from django.urls import path
from . import views


urlpatterns = [
    path('',views.user_landing,name='user_landing'),
    path('user_detail',views.user_detail,name='user_detail'),
    path('user_gift_selection',views.user_gift_selection,name='user_gift_selection'),
    path('user_successful_giftorder',views.user_successful_giftorder,name='user_successful_giftorder'),
    path('distributor_login',views.distributor_login,name='distributor_login'),
    path('distributor_gift_selection',views.distributor_gift_selection,name='distributor_gift_selection'),
    path('distributor_peoplelist',views.distributor_peoplelist,name='distributor_peoplelist'),
    
]
    