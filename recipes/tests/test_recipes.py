from django.test import TestCase


class TestRecipes(TestCase):
    def test_recipe_list(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_recipe_detail(self):
        response = self.client.get("/recipes/1/")
        self.assertEqual(response.status_code, 200)
