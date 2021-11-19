from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # just include the class name to make generic
    path('<int:record_id>/', views.detail, name='detail'),

    path('search/', views.search, name='search'), 

    path('add/', views.add, name = 'add' ), 

    path('saved/', views.saved, name='saved'),

    path('accounts/', include('django.contrib.auth.urls')),
]

