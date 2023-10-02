from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('ajay', views.ajay, name="ajay"),
    path('signup', views.handleSignup, name="handleSignup"),
    path('login', views.handleLogin, name="handleLogin"),
    path('text_operation', views.textOperation, name="textOperation"),
    path('analyze',views.analyze,name='analyze'),
    path('logout', views.handleLogout, name="handleLogout"),
]
