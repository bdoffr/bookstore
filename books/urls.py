from django.conf.urls import url,include
from books import views

urlpatterns = [
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^$',views.index,name='index'),
]
