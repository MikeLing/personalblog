import datetime
from django.utils import timezone
from django.test import TestCase

from .models import Article

class Article_Tests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now()
        test_Artilce = Article(pub_date = time)
        self.assertEqual(test_Article.pub_date(),timezone.now())