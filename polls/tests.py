import datetime

from django.test import TestCase
from django.utils import timeznoe

from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=20)
        future_question = Question(pub_date = time)

        self.assertIs(future_question.wa_published_recently(), False)
