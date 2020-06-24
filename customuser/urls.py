from django.urls import path
from . import views

urlpatterns = [

   path('logout/', views.logout_page, name='logout_page'),
   path('register/', views.register, name='register'),
   path('change_avatar/', views.change_avatar, name='change_avatar'),
   path('new_bet/', views.new_bet, name='new_bet'),
   path('new_payment/', views.new_payment, name='new_payment'),
   path('pay_complete/', views.pay_complete, name='pay_complete'),
   path('add_payment/', views.add_payment, name='add_payment'),
   path('login_req/', views.login_req, name='login_req'),
   path('profile/', views.profile_index, name='profile_index'),
   path('profile/edit', views.profile_edit, name='profile_edit'),
   path('profile/finance', views.profile_finance, name='profile_finance'),
   path('profile/balance', views.profile_balance, name='profile_balance'),
   path('profile/archive', views.profile_archive, name='profile_archive'),


]
