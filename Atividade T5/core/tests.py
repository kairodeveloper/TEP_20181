from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import *
from django.contrib.auth.models import User

class ProfileTest(APITestCase):
    def create(self):
        url = reverse('-list')
        self.user.name = str(self.user.id)
        self.user.save()
        post_data = {'owner': self.profile.id, 'userId': self.user.id,
                     'title': 'New Post', 'body': 'Test hello world!'}
        response = self.client.post(url, post_data, format='json')
        # print("Response: ", response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class GeneralTest(APITestCase):
    def setUp(self):
        User.objects.create(username="kairo", password="kairo123")
        User.objects.create(username="costa", password="costa123")
        Profile.objects.create(name='Kairo Costa', email='kairo@email.com', street='rua teresina', suite='123', city='Teresina', zipcode='123')
        Profile.objects.create(name='Costa Kairo', email='costa@email.com', street='rua teresina', suite='123', city='Teresina', zipcode='123')
        Post.objects.create(title="teste1", body="teste1", profile=Profile.objects.get(id=1), owner=User.objects.get(id=1))
        Post.objects.create(title="teste2", body="teste2", profile=Profile.objects.get(id=2), owner=User.objects.get(id=2))
        Comment.objects.create(post_id=Post.objects.get(id=1), name='Comment 1', body='teste1')
        Comment.objects.create(post_id=Post.objects.get(id=1), name='Comment 2', body='teste2')
        Comment.objects.create(post_id=Post.objects.get(id=2), name='Comment 3', body='teste3')
        Comment.objects.create(post_id=Post.objects.get(id=2), name='Comment 4', body='teste4')

