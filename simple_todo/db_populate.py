from factory import Faker
from factory.django import DjangoModelFactory

from core.models import Post


class AccountFactory(DjangoModelFactory):
    class Meta:
        model = Post
