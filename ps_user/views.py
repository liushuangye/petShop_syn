# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from models import UserInfo
from ps_goods.models import GoodsInfo
from hashlib import sha1#sha1加密

# Create your views here.
#注册界面
def register(request):
    return render(request,'ps_user/register.html')
#注册处理
def register_handle(request):
    #接收用户输入
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    #判断两次密码
    if upwd != upwd2:
        return
    #对密码进行加密
    s1 = sha1()
    s1.update(upwd)
    upwd3 = s1.hexdigest()
    #创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()

    return redirect('/user/login/')

#登录界面
def login(request):
    uname = request.COOKIES.get('uname', '')#cookies中没有则用户名默认为''
    context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 0, 'uname': uname}
    return render(request,'ps_user/login.html',context)

#登录处理
def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu',0)
    #根据uname查表，判断用户名是否存在
    users = UserInfo.objects.filter(uname=uname)
    #
    if len(users)==1:
       s1 = sha1()
       s1.update(upwd)
       if s1.hexdigest() == users[0].upwd:
           url = request.COOKIES.get('url','/')
           red = HttpResponseRedirect(url)
          # red = HttpResponseRedirect('/user/info')
           # 记住用户名
           if jizhu != 0:
               red.set_cookie('uname', uname)
           else:
               red.set_cookie('uname', '', max_age=-1)
           request.session['user_id'] = users[0].id
           request.session['user_name'] = uname
           return red
       else:
           context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': uname, 'upwd': upwd}
           return render(request, 'ps_user/login.html', context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd}
        return render(request, 'ps_user/login.html', context)

#登出处理
def logout(request):
    request.session.flush()
    return redirect('/')
#用户中心
def info(request):
    user_email = UserInfo.objects.get(id=request.session['user_id']).uemail
    user_address = UserInfo.objects.get(id=request.session['user_id']).uaddress
    # 最近浏览
    goods_ids = request.COOKIES.get('goods_ids', '')
    goods_id_list = goods_ids.split(',')
    goods_list = []
    for goods_id in goods_id_list:
        goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))

    context = {'title': '用户中心',
               'user_email': user_email,
               'user_address': user_address,
               'user_name': request.session['user_name'],
               'page_name': 1, 'info': 1,
               'goods_list': goods_list}
    return render(request, 'ps_user/user_center_info.html', context)
#收货地址
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.ucustomer = post.get('ucustomer')
        user.uaddress = post.get('uaddress')
        user.uphone = post.get('uphone')
        user.uyoubian = post.get('uyoubian')
        user.save()
    context = {'title': '用户中心', 'user': user,'page_name':1,'site':1}
    return render(request, 'ps_user/user_center_site.html', context)










