from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('',views.index,name='index'),
    path('pricing',views.pricing,name='pricing'),
    path('payment/<str:email>/<int:sub_id>',views.payment,name='payment'),
    path('pay_test',views.test_pay,name='test_pay'),

    




]