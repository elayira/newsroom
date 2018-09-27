import factory


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'news.Article'
        django_get_or_create = ('id', )

    title = factory.Faker('sentence')
    body = factory.Faker('paragraph')
    id = factory.Faker('uuid4')
