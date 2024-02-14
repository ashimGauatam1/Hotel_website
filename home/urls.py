from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path('signin',views.signin,name='signin'),
   path("contact",views.contact,name='contact'),
   path("staffs",views.staffs,name="staffs"),
   path('',views.main,name='main'),
   path("register",views.register,name="register"),
   path('book',views.book,name='book'),
   path('stafflog',views.stafflog,name='stafflog'),
   path('customerdetails',views.customer_details,name='customer_details'),
   path('deletecustomer/<id>/',views.delete_customer,name='delete_customer'),
   path('logout',views.logoutu,name='logout'),
]