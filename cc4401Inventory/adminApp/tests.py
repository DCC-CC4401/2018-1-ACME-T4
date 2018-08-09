from django.test import TestCase, Client
from django.urls import reverse
from mainApp.models import User


class AdminAppTestCase(TestCase):
    def SetUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(email='some@admin_mail.com', password='somepass',
                                                 first_name='some', last_name='admin', rut='123456789',
                                                 is_staff=True)

    def test_landing_admin_page(self):
        response = self.client.post(reverse('login_submit'),{'email': 'some@admin', 'password': 'somepass'})
        self.assertRedirects(response, reverse('landing-panel'))

