from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from django.db import models
from django.utils import timezone
from datetime import datetime

class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = GameCategory
		fields = ('url', 'pk', 'name', 'games')

class GameSerializer(serializers.HyperlinkedModelSerializer):
	game_category =	serializers.SlugRelatedField(queryset=GameCategory.objects.all(), slug_field='name')

	class Meta:
		model = Game
		fields = ('url', 'game_category', 'name', 'release_date', 'played')

	def validate(self, data):
		if Game.objects.filter(name=data['name']).exists():
			raise serializers.ValidationError("Jogo já existe!")
		return data

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
	game = serializers.SlugRelatedField(queryset=Game.objects.all(), slug_field='name', allow_null=True)
	player = serializers.SlugRelatedField(queryset=Player.objects.all(), slug_field='name', allow_null=True)

	class Meta:
		model = Score
		fields = ('url', 'pk', 'score', 'score_date', 'player', 'game')

	def validate(self, data):
		if data['game'] == None:
			raise serializers.ValidationError('Game não selecionado')
		elif data['player'] == None:
			raise serializers.ValidationError('Player não selecionado')
		elif data['score']==None or data['score'] < 0:
			raise serializers.ValidationError('Score negativo, e/ou nulo!')
		elif data['score_date'] >  timezone.make_aware(datetime.now(),timezone.get_current_timezone()):
			raise serializers.ValidationError('Score no futuro, não permitido!')
		return data

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
	scores = ScoreSerializer(many=True, read_only=True)

	class Meta:
		model = Player
		fields = ('url', 'name', 'gender', 'scores')