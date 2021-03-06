from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from users.models import Passport, Address
import re
from utils.decorators import login_required

def register_handle(request):
    '''进行用户注册处理'''
    # 接收数据
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')

    # 进行数据校验
    if not all([username, password, email]):
        # 有数据为空
        return render(request, 'users/register.html', {'errmsg': '参数不能为空!'})

    # 判断邮箱是否合法
    if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        # 邮箱不合法
        return render(request, 'users/register.html', {'errmsg': '邮箱不合法!'})

    # 进行业务处理:注册，向账户系统中添加账户
    # Passport.objects.create(username=username, password=password, email=email)
    try:
        Passport.objects.add_one_passport(username=username, password=password, email=email)
    except Exception as e:
        print("e:",e)
        return render(request, 'users/register.html', {'errmsg': '用户名已存在！'})

    # 注册完，还是返回注册页。
    return redirect(reverse('books:index'))

def register(request):
    '''显示用户注册页面'''
    return render(request, 'users/register.html')

def login(request):
    '''显示登录页面'''
    if request.COOKIES.get("username"):
        username = request.COOKIES.get("username")
        checked = 'checked'
    else:
        username = ''
        checked = ''
    context = {
        'username': username,
        'checked': checked,
    }

    return render(request, 'users/login.html', context)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_check(request):
    '''进行用户登录校验'''
    # 1.获取数据
    data = request.body.decode('utf8')
    import json
    data = json.loads(data)
    username = data.get('username')
    password = data.get('password')
    remember = data.get('remember')

    # 2.数据校验
    if not all([username, password, remember]):
        # 有数据为空
        return JsonResponse({'res': 2, 'errmsg': 'data cannot be null'})

    # 3.进行处理:根据用户名和密码查找账户信息
    passport = Passport.objects.get_one_passport(username=username, password=password)

    if passport:
        next_url = reverse('books:index')
        jres = JsonResponse({'res': 1, 'next_url': next_url})

        # 判断是否需要记住用户名
        if remember == 'true':
            # 记住用户名
            jres.set_cookie('username', username, max_age=7*24*3600)
        else:
            # 不要记住用户名
            jres.delete_cookie('username')

        # 记住用户的登录状态
        request.session['islogin'] = True
        request.session['username'] = username
        request.session['passport_id'] = passport.id
        return jres
    else:
        # 用户名或密码错误
        return JsonResponse({'res': 0, 'errmsg': 'username or password cannot be wrong.'})
def logout(request):
    '''用户退出登录'''
    # 清空用户的session信息
    request.session.flush()
    # 跳转到首页
    return redirect(reverse('books:index'))
def logout(request):
    '''用户退出登录'''
    # 清空用户的session信息
    request.session.flush()
    # 跳转到首页
    return redirect(reverse('books:index'))
def logout(request):
    '''用户退出登录'''
    # 清空用户的session信息
    request.session.flush()
    # 跳转到首页
    return redirect(reverse('books:index'))


@login_required
def user(request):
    passport_id = request.session.get('passport_id')
    addr = Address.objects.get_default_address(passport_id=passport_id)

    books_li = []
    context = {
        'addr':addr,
        'page':'user',
        'books_li':books_li
}
    return render(request,'users/user_center_info.html',context)


from rest_framework import mixins
from rest_framework import viewsets
from users.serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.GenericViewSet,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin
                        ):
    queryset = Passport.objects.all()
    serializer_class = UserProfileSerializer
