from django.conf.urls import url,include
from books import views
from rest_framework.routers import DefaultRouter
from books.views import BooksViewSet

urlpatterns = [
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^$',views.index,name='index'),
    url(r'^books/(?P<books_id>\d+)$',views.detail,name='detail'),
    url(r'^list/(?P<type_id>\d+)/(?P<page>\d+)/$', views.list, name='list'),
]
