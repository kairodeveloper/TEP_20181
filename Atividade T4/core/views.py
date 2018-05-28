from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.serializers import *


@api_view(['GET', 'POST'])
def UserList(request):

    if request.method=='GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data)

    elif request.method=='POST':

        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid(request.data):
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def UserDetail(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)

    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET','POST'])
def PostByUser(request):

    if request.method=='GET':
        users = User.objects.all()
        user_serializer = PostByUserSerializer(users, many=True)
        return Response(user_serializer.data)

    elif request.method=='POST':

        post_serializer = PostSerializer(data=request.data)

        if post_serializer.is_valid(request.data):
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_201_CREATED)

        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def PostByUserDetail(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_serializer = PostByUserSerializer(user)
        return Response(user_serializer.data)

    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET','POST'])
def PostList(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        posts = user.posts.all()
        post_serializer = PostSerializer(posts, many=True)
        return Response(post_serializer.data)

    elif request.method == 'POST':

        post_serializer = PostDetailSerializer(data=request.data)

        if post_serializer.is_valid(request.data):
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_201_CREATED)

        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET','PUT','DELETE'])
def PostDetail(request, id, id_post):
    try:
        user = User.objects.get(id=id)
        post = Post.objects.get(id=id_post)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if post in user.posts.all():
        # get unico
        if request.method == 'GET':
            post_serializer = PostDetailSerializer(post)
            return Response(post_serializer.data)

        # edita e deleta o post
        elif request.method=='PUT':
            post_serializer = PostDetailSerializer(post, data=request.data)
            if post_serializer.is_valid():
                post_serializer.save()
                return Response(post_serializer.data)
            return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method=='DELETE':
            Comment.objects.filter(post_id=post).delete()
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','POST'])
def CommentList(request, id, id_post):

    try:
        user = User.objects.get(id=id)
        post = Post.objects.get(id=id_post)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if post in user.posts.all():
        # lista e post
        if request.method == 'GET':
            comments = post.comments.all()
            comment_serializer = CommentSerializerDetail(comments, many=True)
            return Response(comment_serializer.data)

        elif request.method == 'POST':

            comment_serializer = CommentSerializerDetail(data=request.data)

            if comment_serializer.is_valid(request.data):
                comment_serializer.save()
                return Response(comment_serializer.data, status=status.HTTP_201_CREATED)

            return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET','PUT','DELETE'])
def CommentDetail(request, id, id_post, id_comment):
    try:
        user = User.objects.get(id=id)
        post = Post.objects.get(id=id_post)
        comment = Comment.objects.get(id=id_comment)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if post in user.posts.all() and comment in post.comments.all():

        # get unico
        if request.method == 'GET':
            comment_serializer = CommentSerializerDetail(comment)
            return Response(comment_serializer.data)

        # edita e deleta o post
        elif request.method == 'PUT':
            comment_serializer = CommentSerializerDetail(comment, data=request.data)
            if comment_serializer.is_valid():
                comment_serializer.save()
                return Response(comment_serializer.data)
            return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def ReportDetailList(request):
    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = ReportAllUserSerializer(users, many=True)
        return Response(user_serializer.data)