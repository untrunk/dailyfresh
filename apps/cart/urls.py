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
from apps.cart.views import CartAddView,CartInfoView,CartUpdateView,CartDeleteView
urlpatterns = [
    url('^add$',CartAddView.as_view(),name='add'),   # 购物车记录添加
    url('^$',CartInfoView.as_view(),name='show'),    # 购物车页面显示
    url('^update$',CartUpdateView.as_view(),name='update'),  # 购物车记录更新
    url('^delete$',CartDeleteView.as_view(),name='delete'),  # 购物车记录删除
]


