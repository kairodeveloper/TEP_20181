from django.urls import path
from django.conf.urls import include
from core.views import *

urlpatterns = [
    path('servidor/profiles/', UserList),
    path('servidor/profiles/<int:id>/', UserDetail),
    path('servidor/profile-posts/', PostByUser),
    path('servidor/profile-posts/<int:id>/', PostByUserDetail),
    path('servidor/profiles/<int:id>/', include([
            path('posts/', PostList),
            path('posts/<int:id_post>/', PostDetail),
            path('posts/<int:id_post>/comments/', CommentList),
            path('posts/<int:id_post>/comments/<int:id_comment>/', CommentDetail),
    ])),
    path('servidor/report/', ReportAllList),
    path('servidor/report/<int:id>', ReportDetailList)
]





'''
#user
{
    "name":"João",
    "email":"joao@email.com",
    "street":"Rua teresina",
    "suite":"20",
    "city":"Teresina",
    "zipcode":"123456"
}


#post
{
    "user_id": 1,
    "title": "Primeiro post",
    "body": "Aqui vai o texto todo"
}


#comment
{
    "name": "Comment1",
    "email": "kairo@email.com",
    "body": "Conteudo",
    "post_id": 1
}

'''
