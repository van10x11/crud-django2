
from django.contrib import admin
from django.urls import path,include
# from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    # path('login/',auth_views.LoginView.as_view(),name='login'),
    # path('logout/',auth_views.LogoutView.as_view(),name='logout'),


    path('',RedirectView.as_view(pattern_name='login')),

    path('login/',views.user_login,name='login'),
    path('logout/<str:username_login>',views.user_logout,name='logout'),


    path('dashboard/',include('dashboard.urls')),
    path('admin/', admin.site.urls),
]
