from django.urls import reverse
from django.forms.models import model_to_dict
from nose.tools import eq_
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
from rest_framework.authtoken.models import Token

from .factories import ArticleFactory
from users.test.factories import UserFactory
from ..models import Article


fake = Faker()


class TestArticleListTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('article-list')
        self.author = UserFactory()
        Token.objects.get_or_create(user=self.author)
        self.article = ArticleFactory.build(author=self.author)

    def test_post_request_with_no_data_and_no_auth_token_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_request_with_no_data_fails(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.author.auth_token}')
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_and_no_auth_token_fails(self):
        response = self.client.post(self.url, data=model_to_dict(self.article))
        eq_(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_request_with_valid_and__auth_token_suceeds(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.author.auth_token}')
        response = self.client.post(self.url, data=model_to_dict(self.article))
        eq_(response.status_code, status.HTTP_201_CREATED)


class TestArticleDetailTestCase(APITestCase):
    """
    Tests /users detail operations.
    """

    def setUp(self):
        self.author1, self.author2 = UserFactory.create_batch(2)
        self.article = ArticleFactory(author=self.author1)
        self.url = reverse('article-detail', kwargs={'pk': self.article.id})
        Token.objects.get_or_create(user=self.author1)
        Token.objects.get_or_create(user=self.author2)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.author1.auth_token}')

    def test_get_request_returns_a_given_article(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_patch_request_author_updates_an_article_suceeds(self):
        new_body = fake.paragraph()
        payload = {'body': new_body}
        response = self.client.patch(self.url, payload, format='json')
        eq_(response.status_code, status.HTTP_200_OK)

        article = Article.objects.get(pk=self.article.id)
        eq_(article.body, new_body)

    def test_patch_request_not_author_updates_an_article_fails(self):
        article = Article.objects.get(pk=self.article.id)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.author2.auth_token}')

        new_title = fake.sentence()
        payload = model_to_dict(article)
        payload['title'] = new_title

        response = self.client.patch(self.url, payload, format='json')
        eq_(response.status_code, status.HTTP_403_FORBIDDEN)
