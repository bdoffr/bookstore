from django.conf.urls import url,include
from users import views
from users.views import UserProfileViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    url(r'^register/$', views.register, name='register'), # 用户注册
    url(r'^register_handle/$', views.register_handle, name='register_handle'),
    url(r'^login/$', views.login, name='login'), # 显示登陆页面
    url(r'^login_check/$',views.login_check,name='login_check'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^$', views.user, name='user'),
]
