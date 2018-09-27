from django.forms.models import model_to_dict
from .factories import ArticleFactory
from django.test import TestCase
from nose.tools import ok_, eq_
from ..serializers import ArticleSeralizer


class TestArticleSerializer(TestCase):
    def setUp(self):
        self.article_data = model_to_dict(ArticleFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = ArticleSeralizer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = ArticleSeralizer(data=self.article_data)
        ok_(serializer.is_valid())
