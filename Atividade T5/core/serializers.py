from rest_framework import serializers
from core.models import *

class CommentSerializerDetail(serializers.ModelSerializer):

    post_id = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='title')

    class Meta:
        model = Comment
        fields = ('id','name','email','body','post_id')

class UserSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Profile
        fields = ('id','name', 'email', 'street', 'suite', 'city', 'zipcode','user')

class PostSerializer(serializers.HyperlinkedModelSerializer):

    # profile = serializers.SlugRelatedField(queryset=Profile.objects.all(), slug_field='name')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ('id','title', 'body','qtd_comments', 'owner')

class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('profile','id','title','body','qtd_comments')

class PostByUserSerializer(serializers.HyperlinkedModelSerializer):

    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('name','email','posts')


class ReportAllUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Profile
        fields = ('id','name','qtd_posts','qtd_comments_by_post')
