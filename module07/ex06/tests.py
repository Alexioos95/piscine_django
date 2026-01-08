from ex06.models import Article, UserFavouriteArticle
from django.utils.translation import activate
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.shortcuts import resolve_url
from django.urls import reverse

class Ex06PermTests(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user(username="QWER", password="qazwsxedcrfv123")
		self.article = Article.objects.create(
			title="abc",
			synopsis="def",
			content="ghi",
			author=self.user
		)

	def test_favourites_requires_login(self):
		response = self.client.get(reverse("ex06:favourites"))
		self.assertNotEqual(response.status_code, 200)
		login_url = resolve_url('ex06:login')
		expected_url = f"{login_url}?next={reverse('ex06:favourites')}"
		self.assertRedirects(response, expected_url)

	def test_publications_requires_login(self):
		response = self.client.get(reverse("ex06:publications"))
		self.assertNotEqual(response.status_code, 200)
		login_url = resolve_url('ex06:login')
		expected_url = f"{login_url}?next={reverse('ex06:publications')}"
		self.assertRedirects(response, expected_url)

	def test_publish_requires_login(self):
		response = self.client.get(reverse("ex06:publish"))
		self.assertNotEqual(response.status_code, 200)
		login_url = resolve_url('ex06:login')
		expected_url = f"{login_url}?next={reverse('ex06:publish')}"
		self.assertRedirects(response, expected_url)

	def test_logged_access_register(self):
		self.client.login(username="QWER", password="qazwsxedcrfv123")
		response = self.client.get(reverse("ex06:register"))
		self.assertNotEqual(response.status_code, 200)
		self.assertIn(response.status_code, (302, 403))

class Ex06FavTests(TestCase):
	def setUp(self):
		activate("en")
		self.client = Client()
		self.user = User.objects.create_user(username="QWER2", password="qazwsxedcrfv123")
		self.client.login(username="QWER2", password="qazwsxedcrfv123")
		self.article = Article.objects.create(
			title="abc",
			synopsis="def",
			content="ghi",
			author=self.user
		)
		self.add_url = reverse("ex06:add_favourite", kwargs={"pk": self.article.pk})

	def test_duplicate_favorite(self):
		self.client.post(self.add_url, data={})
		response = self.client.post(self.add_url, data={})
		favourites = UserFavouriteArticle.objects.filter(user=self.user, article=self.article)
		self.assertEqual(favourites.count(), 1)
		self.assertRedirects(response, reverse("ex06:favourites"))
