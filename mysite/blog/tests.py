from django.test import TestCase, Client
from .models import Article
from django.urls import reverse

class ArticleTestCase(TestCase):

    def setUp(self):
        Article.objects.create(
            title= 'Some title',
            description= 'Some description',
            author = 'silver'
            )

    def test_article_exist(self):
        """ some doing"""
        article = Article.objects.get(title='Some title')
        self.assertEqual(article.author, 'silver')

class ArticleCreateViewTest(TestCase):

    def setUp(self):
        client= Client()

    def test_article_created(self):
        """ test_client"""
        response = self.client.post(
            reverse('add_article'), {'title':'Test title', 'description': 'Some description', 'author' :'silver'}
        )

        self.assertEqual(response.status_code, 302)
