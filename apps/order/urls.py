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
from apps.order.views import OrderPlaceView,OrderCommitView,OrderPayView,CheckPayView

urlpatterns = [
    url('^place$',OrderPlaceView.as_view(),name='place'), #订单显示页面
    url('^commit$',OrderCommitView.as_view(),name='commit'), #订单创建
    url('^pay$',OrderPayView.as_view(),name='pay'), #支付
    url('^check$',CheckPayView.as_view(),name='check') # 支付状态
]


