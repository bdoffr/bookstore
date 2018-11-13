from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'), # 用户注册
    url(r'^register_handle/$', views.register_handle, name='register_handle'),
    url(r'^login/$', views.login, name='login') # 显示登陆页面
]
