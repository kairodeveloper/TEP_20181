from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.throttling import ScopedRateThrottle
from core.permissions import *
from core.serializers import *


class UserList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    permission_classes = (IsAuthenticated, OnlySafeMethods)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    permission_classes = (IsAuthenticated, OnlySafeMethods)


class PostByUser(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = PostByUserSerializer
    name = 'post-by-user'
    permission_classes = (IsAuthenticated, OnlySafeMethods)


class PostByUserDetail(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    name = 'user-posts-list'
    http_method_names = ['get']
    permission_classes = (IsAuthenticated, OnlySafeMethods)


    def get_queryset(self):
        return Post.objects.filter(profile=self.kwargs['pk'])


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    name = 'post-list'
    http_method_names = ['get','post']
    permission_classes = (IsAuthenticated, OnlySafeMethods)

    def get_queryset(self):
        profile = Profile.objects.get(id=self.kwargs['pk'])
        return Post.objects.filter(profile=profile, owner=profile.user)

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(owner=self.request.user, profile=profile)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    name = 'post-detail-serializer'
    permission_classes = (IsAuthenticated, OnlyOwnerCanDoIt)

    def get_queryset(self):
        profile = Profile.objects.get(id=self.kwargs['pkid'])
        return Post.objects.filter(id=self.kwargs['pk'], profile=profile)

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializerDetail
    name = 'comment-list'
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['pkid'])

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializerDetail
    name = 'comment-detail'
    permission_classes = (IsAuthenticated, OnlyOwnerCanDestroyComments)

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['pkid'])


class ReportAllList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ReportAllUserSerializer
    name = 'report'
    permission_classes = (IsAuthenticated,)


class ReportDetailList(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Profile.objects.all()
    serializer_class = ReportAllUserSerializer
    name = 'report_detailed'
    permission_classes = (IsAuthenticated,)


class PostObtainToken(ObtainAuthToken):

    throttle_scope = 'obtain-token'
    throttle_classes = (ScopedRateThrottle,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username
        })

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
                'profiles': reverse(UserList.name, request=request),
                'report': reverse(ReportAllList.name, request=request),
            }
        )