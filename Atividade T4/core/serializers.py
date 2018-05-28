from rest_framework import serializers
from core.models import *

class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = ('name','email')

class CommentSerializerDetail(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id','name','email','body','post_id')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'email', 'street', 'suite', 'city', 'zipcode')

    def is_valid(self, data):
        if User.objects.filter(name=data['name']).exists():
            raise serializers.ValidationError("Usuário com esse nome já existe!")
        return data

class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ('id','title', 'body','qtd_comments')

class PostDetailSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, read_only=True)


    class Meta:
        model = Post
        fields = ('user_id','id','title','body','comments')

class PostByUserSerializer(serializers.HyperlinkedModelSerializer):

    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('name','email','posts')


class ReportAllUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id','name','qtd_posts','qtd_comments_by_post')
