from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class PublicKitchenTests(TestCase):
    def test_login_required_for_index(self):
        res = self.client.get(reverse("kitchen:index"))
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_for_dish_list(self):
        res = self.client.get(reverse("kitchen:dish-list"))
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_for_cook_list(self):
        res = self.client.get(reverse("kitchen:cook-list"))
        self.assertNotEqual(res.status_code, 200)


class PrivateKitchenTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testcook",
            password="password123"
        )
        self.client.login(username="testcook", password="password123")

    def test_index_page_accessible_for_logged_in_user(self):
        res = self.client.get(reverse("kitchen:index"))
        self.assertEqual(res.status_code, 200)

    def test_dish_list_accessible_for_logged_in_user(self):
        res = self.client.get(reverse("kitchen:dish-list"))
        self.assertEqual(res.status_code, 200)
