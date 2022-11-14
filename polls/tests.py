import datetime

from django.test import TestCase
from django.utils import timezone
from datetime import datetime,timedelta

from .models import Question
# Create your tests here.

#se testean modelos o vistas
class QuestionModelTests(TestCase):

    def setUp(self):
        self.question = Question(question_text = "Quien es el mejor course director de platzy")

    def test_was_publish_recently_with_future_questions(self):
        """ was_published_recently returns False for question whose pub_date is in the future """
        time = timezone.now() + timedelta(days = 30)
        self.question.pub_date = time
        self.assertIs(self.question.was_published_recently(),False)

    def test_was_publish_recently_with_present_questions(self):
        """ was_published_recently returns True for question whose pub_date is now """
        time = timezone.now() - timedelta(hours = 23)
        self.question.pub_date = time
        self.assertIs(self.question.was_published_recently(),True)

    def test_was_publish_recently_with_past_questions(self):
        """ was_published_recently returns False for question whose pub_date is in the past """
        time = timezone.now() - timedelta(days=1, minutes=1)
        self.question.pub_date = time
        self.assertIs(self.question.was_published_recently(),False)


