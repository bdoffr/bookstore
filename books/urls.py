from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'^&',views.index,name='index',
    url(r'^tinymce/', include('tinymce.urls')),
]