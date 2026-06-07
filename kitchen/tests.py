from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Dish, DishType


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

        self.dish_type = DishType.objects.create(name="Soup")
        self.dish = Dish.objects.create(
            name="Borscht",
            description="Traditional soup",
            price=10.50,
            dish_type=self.dish_type
        )

    def test_index_page_accessible_for_logged_in_user(self):
        res = self.client.get(reverse("kitchen:index"))
        self.assertEqual(res.status_code, 200)

    def test_dish_list_accessible_for_logged_in_user(self):
        res = self.client.get(reverse("kitchen:dish-list"))
        self.assertEqual(res.status_code, 200)

    def test_dish_detail_view(self):
        res = self.client.get(
            reverse("kitchen:dish-detail", kwargs={"pk": self.dish.id})
        )
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.dish.name)

    def test_dish_create_view_post(self):
        form_data = {
            "name": "New Dish",
            "description": "Delicious",
            "price": 15.00,
            "dish_type": self.dish_type.id,
            "cooks": [self.user.id]
        }
        res = self.client.post(reverse("kitchen:dish-create"), data=form_data)
        self.assertEqual(res.status_code, 302)
        self.assertTrue(Dish.objects.filter(name="New Dish").exists())

    def test_toggle_assign_to_dish(self):
        url = reverse(
            "kitchen:toggle-dish-assign",
            kwargs={"pk": self.dish.id}
        )
        self.client.post(url)
        self.assertIn(self.user, self.dish.cooks.all())

        self.client.post(url)
        self.assertNotIn(self.user, self.dish.cooks.all())

    def test_dish_delete_view_post(self):
        url = reverse("kitchen:dish-delete", kwargs={"pk": self.dish.id})
        res = self.client.post(url)
        self.assertEqual(res.status_code, 302)
        self.assertFalse(Dish.objects.filter(id=self.dish.id).exists())

    def test_dish_list_pagination(self):
        for i in range(10):
            Dish.objects.create(
                name=f"Dish {i}",
                price=5.00,
                dish_type=self.dish_type
            )
        res = self.client.get(reverse("kitchen:dish-list"))
        self.assertEqual(res.status_code, 200)
        self.assertIn("is_paginated", res.context)
        self.assertEqual(len(res.context["dish_list"]), 5)
