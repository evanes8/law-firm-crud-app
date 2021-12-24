from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from . import api_views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # just include the class name to make generic
    path('<int:record_id>/', views.detail, name='detail'),

    path('search/', views.search, name='search'), 

    path('add/', views.add, name = 'add' ), 

    path('saved/', views.saved, name='saved'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('records_api/', api_views.RecordList.as_view()), 

    path('records_api/<int:pk>/', api_views.RecordDetail.as_view()),

    path('contacts_api/', api_views.ContactList.as_view()),

    path('relationships_api/', api_views.RelationshipList.as_view()),

    path('related_contacts_api/<int:pk>/', api_views.RelatedContactList.as_view()),

    path('test/', views.test, name='test'),


]


urlpatterns = format_suffix_patterns(urlpatterns)
