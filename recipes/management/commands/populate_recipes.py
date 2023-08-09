from random import choices

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError, CommandParser
from django.db.utils import OperationalError

from recipes.models import Category, Recipe
from recipes.utils.factory import RECIPES


class Command(BaseCommand):
    help = "Populates the database with recipes"

    def recipe_data_exists(self):
        try:
            return Recipe.objects.count() > 0
        except OperationalError as e:
            raise CommandError("Verifique se o modelo Recipes foi migrado corretamente e tente novamente!") from e

    def get_categories(self):
        categories = Category.objects.all()
        if not categories:
            categories = [
                Category(name="Café da manhã"),
                Category(name="Almoço"),
                Category(name="Jantar"),
                Category(name="Sobremesa"),
                Category(name="Lanche"),
            ]
            Category.objects.bulk_create(categories)
            categories = Category.objects.all()
        return categories

    def get_users(self):
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
            recipe = Recipe(
                title=r["title"],
                description=r["description"],
                slug=r["slug"],
                preparation_time=r["preparation_time"],
                preparation_time_unit=r["preparation_time_unit"],
                servings=r["servings"],
                servings_unit=r["servings_unit"],
                preparation_steps=r["preparation_steps"],
                preparation_steps_is_html=r["preparation_steps_is_html"],
                is_published=r["is_published"],
                cover=r["cover"],
                category=choices(categories)[0],
                author=choices(authors)[0],
            )
            recipe.save()
            self.stdout.write(f"Recipe {recipe.title} created")
        self.stdout.write(self.style.SUCCESS(f"{len(RECIPES)} Recipes created successfully!"))
