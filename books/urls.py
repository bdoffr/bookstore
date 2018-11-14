from django.conf.urls import url,include
from books import views

urlpatterns = [
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^$',views.index,name='index'),
    url(r'^books/(?P<books_id>\d+)$',views.detail,name='detail')
]
