from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[path('',views.main,name="main"),path('patients/',views.patient,name="patient"),path('doctors/',views.patient,name='patient'),path('patients/login',views.login,name='login'),path('doctors/login',views.login,name='login')]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)