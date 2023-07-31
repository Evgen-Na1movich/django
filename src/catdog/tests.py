from django.test import TestCase
from django.urls import reverse
from catdog.models import AnimalImage


class TestModelAnimalImage(TestCase):
    pass



class TestCatDogView(TestCase):

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

    def test_dog_post(self):
        response = self.client.post(reverse('catdog'), {'dog': True})
        """проверка на равенство. сравниваем код ответа  с кодом 200"""
        self.assertEqual(response.status_code, 200)
        """проверяет, что при рендеринге страницы использовался указанный шаблон"""
        self.assertTemplateUsed(response, template_name='pet.html')

    def test_reise(self):
        with self.assertRaisesMessage(ValueError, "invalid literal for int()"):
            int("a")