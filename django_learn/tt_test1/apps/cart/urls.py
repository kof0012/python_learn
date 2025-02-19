from apps.cart.views import *
from django.urls import re_path

app_name = 'cart'
urlpatterns = [
    re_path(r'^add$', CartAddView.as_view(), name='add'),  # 添加购物车记录
    re_path(r'^$', CartInfoView.as_view(), name='show'),  # 购物车页面显示
    re_path(r'^update$', CartUpdateView.as_view(), name='update'),  # 购物车记录更新
    re_path(r'^delete$', CartDeleteView.as_view(), name='delete'),  # 购物车记录删除
]
