# from inspect import signature
from random import randint

from faker import Faker


def rand_ratio():
    return f"{randint(840, 900)}/{randint(473, 573)}"


fake = Faker("pt_BR")
# print(signature(fake.random_number))


def make_recipe(qtty=1):
    recipes = []
    for _ in range(qtty):
        r = {}
        r["title"] = fake.sentence(nb_words=6)
        r["description"] = fake.sentence(nb_words=12)
        r["preparation_time"] = fake.random_number(digits=2, fix_len=True)
        r["preparation_time_unit"] = "Minuto" if r["preparation_time"] == 1 else "Minutos"
        r["servings"] = fake.random_number(digits=2, fix_len=True)
        r["servings_unit"] = "Porção" if r["servings"] == 1 else "Porções"
        r["preparation_steps"] = fake.text(3000)
        r["created_at"] = fake.date_time()
        r["author"] = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
        }
        r["category"] = {"name": fake.word()}
        r["cover"] = {
            "url": f"https://loremflickr.com/{rand_ratio()}/food,cook",
        }
        recipes.append(r)

    return recipes[0] if qtty == 1 else recipes


if __name__ == "__main__":
    from pprint import pprint

    pprint(make_recipe())
