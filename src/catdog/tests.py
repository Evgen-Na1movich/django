from django.test import TestCase, Client
from django.urls import reverse
from catdog.models import AnimalImage


class TestModelAnimalImage(TestCase):
    pass


class TestCatDogView(TestCase):
    fixtures = ['data_for_test.json']

    def setUp(self):
        self.client = Client()
        self.assertEqual(AnimalImage.objects.count(), 25)

    def test_get(self):
        response = self.client.get(reverse('catdog'))
        """проверка на равенство. сравниваем ответ от сервера с кодом 200"""
        self.assertEqual(response.status_code, 200)
        """проверяет, что при рендеринге страницы использовался указанный шаблон"""
        self.assertTemplateUsed(response, template_name='catdog.html')

    def test_cat_post(self):
        response = self.client.post(reverse('catdog'), {'cat': True})
        """проверка на равенство. сравниваем код ответа  с кодом 200"""
        self.assertEqual(response.status_code, 200)
        """проверяет, что при рендеринге страницы использовался указанный шаблон"""
        self.assertTemplateUsed(response, template_name='pet.html')
        """тестирование на создание сессии"""
        self.assertEqual(self.client.session['data_for_session']['speicies'], 'cat')

    def test_dog_post(self):
        response = self.client.post(reverse('catdog'), {'dog': True})
        """проверка на равенство. сравниваем код ответа  с кодом 200"""
        self.assertEqual(response.status_code, 200)
        """проверяет, что при рендеринге страницы использовался указанный шаблон"""
        self.assertTemplateUsed(response, template_name='pet.html')

    def test_reise(self):
        with self.assertRaisesMessage(AttributeError, ' at home'):
            self.client.post(reverse('catdog'), {'gg': True})

    def test_save_catdog(self):
        self.client.post(reverse('catdog'), {'cat': True})
