from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from articlesApp.models import Article
from loansApp.models import Loan
from mainApp.models import User
from reservationsApp.models import Reservation
from spacesApp.models import Space


class MainAppTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.articles = []
        for i in range(5):
            self.articles.append(Article.objects.create(name='article' + str(i)))
        self.user = User.objects.create_user(email='email@email.com', password='pass')
        self.assertTrue(self.client.login(email='email@email.com', password='pass'))
        space = Space.objects.create()
        self.reservation = Reservation.objects.create(user=self.user, space=space, starting_date_time=timezone.now(),
                                                      ending_date_time=timezone.now())

    def test_landing_page(self):
        response = self.client.post(reverse('login_submit'), {'email': 'email@email.com', 'password': 'pass'})
        self.assertRedirects(response, reverse('landing_articles'))

    def test_article_has_id(self):
        for article in self.articles:
            self.assertTrue(article.get_id() is not None)

    def test_reservation_has_id(self):
        self.assertTrue(self.reservation.get_id() is not None)

    def test_basic_search(self):
        response = self.client.get(reverse('search'), {'query': 'article', 'estado': 'A'})
        self.assertEquals(len(self.articles), len(response.context['productos']))
        response = self.client.get(reverse('search'), {'query': 'article0', 'estado': 'A'})
        self.assertEquals(self.articles[0], response.context['productos'][0])

    def test_user_can_make_loan(self):
        date = timezone.now().date() + timezone.timedelta(days=1)
        if date.isoweekday() >= 6:
            date += timezone.timedelta(days=2)
        self.client.post(reverse('article_request'), {'article_id': self.articles[0].id,
                                                      'hora_inicio': '13:00',
                                                      'hora_fin': '15:00',
                                                      'fecha_inicio': date.isoformat(),
                                                      'fecha_fin': date.isoformat()})
        loans = Loan.objects.filter(user=self.user)
        self.assertEquals(1, len(loans))
