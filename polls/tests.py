import datetime

from django.test import TestCase
from django.utils import timezone
from datetime import datetime,timedelta
from django.urls.base import reverse

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


def create_question(question_text, days):
    """
    Create a question with the given "question_text", and published the given number
    of days offset to now (negative for question published in the past,
    positive for question that have yet to be published)
    """
    time = timezone.now() + timedelta(days = days)
    return Question.objects.create(question_text=question_text,pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """ if no question exist, an appropiate message is displayed """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"],[])
    
    def test_future_question(self):
        """
        Question with a pub_date in the future aren't displayed on te index page
        """
        create_question("Future question",days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response,"No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"],[])


    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the index page
        """
        question = create_question("Past Question",days=-10)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"],[question])





