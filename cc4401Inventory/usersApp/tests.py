from django.test import TestCase, Client
from django.urls import reverse

from mainApp.models import User


class UserAppTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email='email@email.com', password='pass', first_name='abc',
                                             last_name='def', rut='123456789', enabled=True)
        self.client.login(email='email@email.com', password='pass')

    def test_check_user_data(self):
        response = self.client.get(reverse('user_data', kwargs={'user_id': self.user.id}))
        self.assertEquals(self.user, response.context['user'])

    def test_remove_reservations(self):
        pass
