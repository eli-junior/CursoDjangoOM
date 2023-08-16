from random import choices

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError, CommandParser
from django.db.utils import OperationalError

from recipes.models import Category, Recipe
from recipes.utils.factory import RECIPES


class Command(BaseCommand):
    help = "Populates the database with recipes"

    users_data = [
        {
            "username": "ana",
            "email": "ana@localhost",
            "password": "ana123",
            "first_name": "Ana",
            "last_name": "Ficticia",
        },
        {
            "username": "joao",
            "email": "joao@localhost",
            "password": "jao123",
            "first_name": "João",
            "last_name": "Imaginário",
        },
    ]

    categories_data = ["Café da manhã", "Almoço", "Jantar", "Sobremesa", "Lanche"]

    def recipe_data_exists(self):
        try:
            return Recipe.objects.count() > 0
        except OperationalError as e:
            raise CommandError("Verifique se o modelo Recipes foi migrado corretamente e tente novamente!") from e

    def get_categories(self):
        if categories := Category.objects.all():
            return categories

        Category.objects.bulk_create([Category(name=category) for category in self.categories_data])

        return Category.objects.all()

    def get_users(self):
        if users := User.objects.all():
            if len(users) > 1:
                return users

        for user in self.users_data:
            User.objects.create_user(**user)
        return User.objects.all()

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--force",
            "-f",
            action="store_true",
            help="Clean all data and populate the database with recipes",
        )

    def handle(self, *args, **options):
        if self.recipe_data_exists():
            if not options["force"]:
                error = "Recipes table is not empty. Use --force to clean all data and populate the database with recipes"
                raise CommandError(error)
            else:
                Category.objects.all().delete()
                Recipe.objects.all().delete()
                self.stdout.write(self.style.WARNING("Recipes and Categories table cleaned"))

        categories = self.get_categories()
        authors = self.get_users()

        for r in RECIPES:
            r["category"] = choices(categories)[0]
            r["author"] = choices(authors)[0]
            recipe = Recipe(**r)
            recipe.save()
            self.stdout.write(f"Recipe {recipe.title} created")
        self.stdout.write(self.style.SUCCESS(f"{len(RECIPES)} Recipes created successfully!"))
