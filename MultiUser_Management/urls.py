"""MultiUser_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from MultiUser_Management import settings
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('registration/', views.registration, name="registration"),
    path('login/', views.userlogin, name="userlogin"),
    path('profile/', views.userprofile, name="userprofile"),
    path('saveprofile/', views.saveprofile, name="saveprofile"),
    path('s_panel/', views.student_panel, name="s_panel"),
    path('t_panel/', views.teacher_panel, name="t_panel"),
    path('i_panel/', views.intitute_panel, name="i_panel"),
    path('logout/', views.userlogout, name="logout"),
    path('notes/', views.notes, name="notes"),
    path('que_paper/', views.que_paper, name="que_paper"),
    path('model_papers/', views.model_papers, name="model_papers"),
    path('complete_profile/',views.complete_profile,name="cprofile")


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)