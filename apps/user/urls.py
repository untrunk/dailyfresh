"""dailyfresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required
from apps.user.views import RegisterView,ActiveView,LoginView,UserInfoView,UserOrderView,AddressView,LogoutView

urlpatterns = [
    url('^register$',RegisterView.as_view(),name='register'),  #注册
    url('^active/(?P<token>.*)$',ActiveView.as_view(),name='active'),   #用户激活
    url('^login$',LoginView.as_view(),name='login'),   #登录
    url('^logout$',LogoutView.as_view(),name='logout'),   #登出

    # url('^$',login_required(UserInfoView.as_view()),name='user'),   #用户中心信息
    # url('^order$',login_required(UserOrderView.as_view()),name='order'),   #用户订单
    # url('^address$',login_required(AddressView.as_view()),name='address'),   #用户地址

    #引入LoginMixin之后，类在utils目录下
    url('^$',UserInfoView.as_view(),name='user'),   #用户中心信息
    url('^order/(?P<page>\d+)$',UserOrderView.as_view(),name='order'),   #用户订单
    url('^address$',AddressView.as_view(),name='address'),   #用户地址
]


