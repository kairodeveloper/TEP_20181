# coding=utf-8
from django.urls import path
from django.conf.urls import include
from core.views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', ApiRoot.as_view(), name=ApiRoot.name),

    path('servidor/profiles/', UserList.as_view(), name=UserList.name),
    path('servidor/profiles/<int:pk>/', UserDetail.as_view(), name=UserDetail.name),
    path('servidor/profiles/<int:pk>/posts/', PostList.as_view(), name=PostList.name),
    path('servidor/profiles/<int:pkid>/posts/<int:pk>/', PostDetail.as_view(), name=PostDetail.name),
    path('servidor/profiles/<int:pk>/posts/<int:pkid>/comments/', CommentList.as_view(), name=CommentList.name),
    path('servidor/profiles/<int:id>/posts/<int:pkid>/comments/<int:pk>/', CommentDetail.as_view(), name=CommentDetail.name),

    path('servidor/profile-posts/', PostByUser.as_view(), name=PostByUser.name),
    path('servidor/profile-posts/<int:pk>/', PostByUserDetail.as_view(), name=PostByUserDetail.name),

    path('servidor/report/', ReportAllList.as_view(), name=ReportAllList.name),
    path('servidor/report/<int:pk>', ReportDetailList.as_view(), name=ReportDetailList.name),

    path('servidor/getapitoken/', PostObtainToken.as_view())
]
