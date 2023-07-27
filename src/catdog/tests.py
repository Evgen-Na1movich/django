from django.test import TestCase
from django.urls import reverse


class TestCatDogView(TestCase):

    def test_get(self):
        responce = self.client.get(reverse('catdog'))
        self.assertTemplateUsed(responce, template_name='catdog.html')
