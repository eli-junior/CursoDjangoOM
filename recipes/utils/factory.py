# from inspect import signature
from random import randint

from faker import Faker


def rand_ratio():
    return f"{randint(840, 900)}/{randint(473, 573)}"


fake = Faker("pt_BR")


def make_recipe(qtty=1) -> list[dict] | dict:
    """
    Make a fake recipe or a list of recipes
    """
    recipes = []
    for _ in range(qtty):
        r = {"id": fake.random_number(digits=3, fix_len=True)}
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


RECIPES = [  # skip: E501
    {
        "title": "Bolo de cenoura",
        "description": "Bolo de cenoura com cobertura de chocolate",
        "slug": "bolo-de-cenoura",
        "preparation_time": 40,
        "preparation_time_unit": "Minutos",
        "servings": 8,
        "servings_unit": "fatias",
        "preparation_steps": """
            <ol>
            <li class="grid recipe-steps-item" id="recipe-step1"><div class="is-12 is-12-tablet">
            <span class="recipe-steps-position">1</span><h3 class="recipe-steps-title">Massa</h3>
            <div class="recipe-steps-text">
            <p>Em um liquidificador, adicione a cenoura, os ovos e o óleo, depois misture.</p></div></div></li>
            <li class="no-print">
            <div id="ads-pholder-rectangle_mtf-tablet"></div>
            </li>
            <li class="grid recipe-steps-item" id="recipe-step2"><div class="is-12 is-12-tablet">
            <span class="recipe-steps-position">2</span><div class="recipe-steps-text">
            <p>Acrescente o açúcar e bata novamente por 5 minutos.</p></div></div></li>
            <li class="grid recipe-steps-item" id="recipe-step3"><div class="is-12 is-12-tablet">
            <span class="recipe-steps-position">3</span><div class="recipe-steps-text">
            <p>Em uma tigela ou na batedeira, adicione a farinha de trigo e depois misture novamente</a>.</p></div></div></li>
            <li class="grid recipe-steps-item" id="recipe-step4"><div class="is-12 is-12-tablet">
            <span class="recipe-steps-position">4</span><div class="recipe-steps-text">
            <p>Acrescente o fermento e misture lentamente com uma colher.</p></div></div></li>
            <li class="grid recipe-steps-item" id="recipe-step5"><div class="is-12 is-12-tablet">
            <span class="recipe-steps-position">5</span><div class="recipe-steps-text">
            <p>Asse em um forno preaquecido a 180° C por aproximadamente 40 minutos.</p></div></div></li>
            <li class="grid recipe-steps-item" id="recipe-step6"><div class="is-12 is-12-tablet">
            <span class="recipe-steps-position">6</span><h3 class="recipe-steps-title">Cobertura</h3>
            <div class="recipe-steps-text">
            <p>Despeje em uma tigela a manteiga, o chocolate em pó, o açúcar e o leite, depois misture.</p></div></div></li>
            <li class="no-print u-hidden-desk">
            </li><li class="grid recipe-steps-item" id="recipe-step7"><div class="is-12 is-12-tablet">
            <span class="recipe-steps-position">7</span><div class="recipe-steps-text">
            <p>Leve a mistura ao fogo e continue misturando até obter uma consistência cremosa, depois despeje a calda por cima do bolo</a>.
            </p></div></div></li>
            </ol>
        """,
        "preparation_steps_is_html": True,
        "is_published": True,
        "cover": "recipes/covers/2023/01/01/bolo-de-cenoura.webp",
        "category": "",
        "author": "",
    },
    {
        "title": "Bolo de chocolate",
        "description": "Bolo de chocolate com cobertura de chocolate",
        "slug": "bolo-de-chocolate",
        "preparation_time": 40,
        "preparation_time_unit": "Minutos",
        "servings": 8,
        "servings_unit": "fatias",
        "preparation_steps": """
            <ol>
            <li class="grid recipe-steps-item" id="recipe-step1"><div class="is-12 is-12-tablet">
            <span class="recipe-steps-position">1</span><h3 class="recipe-steps-title">Massa</h3>
            <div class="recipe-steps-text">
            <p>Em um liquidificador adicione os ovos, o chocolate em pó, a manteiga, a farinha de trig
            o, o açúcar e o leite, depois bata por 5 minutos</a>.</p></div></div></li>
            <li class="no-print">
            <div id="ads-pholder-rectangle_mtf-tablet"></div>
            </li>
            <li class="grid recipe-steps-item" id="recipe-step2"><div class="is-12 is-12-tablet">
            <span class="recipe-steps-position">2</span><div class="recipe-steps-text">
            <p>Adicione o fermento e misture com uma espátula delicadamente.</p></div></div></li>
            <li class="grid recipe-steps-item" id="recipe-step3"><div class="is-12 is-12-tablet">
            <span class="recipe-steps-position">3</span><div class="recipe-steps-text">
            <p>Em uma forma untada, despeje a massa e asse em forno médio (180 ºC) preaquecido por cerca de 40 minutos.
            Não se esqueça de usar uma forma alta para essa receita: como leva duas colheres de fermento,
            ela cresce bastante! Outra solução pode ser colocar apenas uma colher de fermento e manter a
            sua receita em uma forma pequena.</p></div></div></li>
            <li class="no-print u-hidden-desk">
            </li><li class="grid recipe-steps-item" id="recipe-step4"><div class="is-12 is-12-tablet">
            <span class="recipe-steps-position">4</span><div class="recipe-steps-text">
            <p>Acrescente o creme de leite e misture bem até obter uma consistência cremosa.</p></div></div></li>
            <li class="grid recipe-steps-item" id="recipe-step5"><div class="is-12 is-12-tablet">
            <span class="recipe-steps-position">5</span><h3 class="recipe-steps-title">Calda</h3>
            <div class="recipe-steps-text">
            <p>Em uma panela, aqueça a manteiga e misture o chocolate em pó até que esteja homogêneo.</p></div></div></li>
            <li class="grid recipe-steps-item" id="recipe-step6"><div class="is-12 is-12-tablet">
            <span class="recipe-steps-position">6</span><div class="recipe-steps-text">
            <p>Desligue o fogo e acrescente o açúcar.</p></div></div></li>
            </ol>
        """,
        "preparation_steps_is_html": True,
        "is_published": True,
        "cover": "recipes/covers/2023/01/01/bolo-chocolate-simples-1.jpg",
        "category": "",
        "author": "",
    },
    {
        "title": "Bobó de camarão",
        "description": (
            "Um clássico da culinária brasileira preparado na sua cozinha: hoje você vai aprender como fazer bobó de camarão! "
            "Essa receita é simples, tradicional e é ideal para um almoço inesquecível em família!"
        ),
        "slug": "bobo-de-camarao",
        "preparation_time": 60,
        "preparation_time_unit": "Minutos",
        "servings": 6,
        "servings_unit": "Porções",
        "preparation_steps": """
            <ol>
                <li class="grid recipe-steps-item" id="recipe-step1"><div class="is-12 is-12-tablet">
                <span class="recipe-steps-position">1</span><div class="recipe-steps-text">
                <p>Lave os camarões e tempere com sal, alho, pimenta e limão, deixe marinar.</p></div></div></li>
                <li class="no-print">
                <div id="ads-pholder-rectangle_mtf-tablet"></div>
                </li>
                <li class="grid recipe-steps-item" id="recipe-step2"><div class="is-12 is-12-tablet">
                <span class="recipe-steps-position">2</span><div class="recipe-steps-text">
                <p>Pegue uma panela com água e cozinhe a mandioca em pedacinhos, com louro e a cebola em rodelas.</p></div></div></li>
                <li class="grid recipe-steps-item" id="recipe-step3"><div class="is-12 is-12-tablet">
                <span class="recipe-steps-position">3</span><div class="recipe-steps-text">
                <p>Quando estiver mole, acrescente um vidro de leite de coco.</p></div></div></li>
                <li class="grid recipe-steps-item" id="recipe-step4"><div class="is-12 is-12-tablet">
                <span class="recipe-steps-position">4</span><div class="recipe-steps-text">
                <p>Deixe esfriar um pouco e bata no liquidificador.</p></div></div></li>
                <li class="grid recipe-steps-item" id="recipe-step5"><div class="is-12 is-12-tablet">
                <span class="recipe-steps-position">5</span><div class="recipe-steps-text">
                <p>Esquente o azeite de oliva, junte a cebola ralada e deixe dourar.</p></div></div></li>
                <li class="grid recipe-steps-item" id="recipe-step6"><div class="is-12 is-12-tablet">
                <span class="recipe-steps-position">6</span><div class="recipe-steps-text">
                <p>Acrescente os camarões e frite.</p></div></div></li>
                <li class="no-print u-hidden-desk">
                </li><li class="grid recipe-steps-item" id="recipe-step7"><div class="is-12 is-12-tablet">
                <span class="recipe-steps-position">7</span><div class="recipe-steps-text">
                <p>Adicione as 2 latas de pomarola, o cheiro-verde, o pimentão e deixe cozinhar por alguns minutos.</p></div></div></li>
                <li class="grid recipe-steps-item" id="recipe-step8"><div class="is-12 is-12-tablet">
                <span class="recipe-steps-position">8</span><div class="recipe-steps-text">
                <p>Junte na mesma panela, a mandioca batida no liquidificador, outro vidro de leite de coco e o azeite de dendê.</p>
                </div></div></li>
                <li class="grid recipe-steps-item" id="recipe-step9"><div class="is-12 is-12-tablet">
                <span class="recipe-steps-position">9</span><div class="recipe-steps-text">
                <p>Deixe levantar fervura e está pronto.</p></div></div></li>
                </ol>
        """,
        "preparation_steps_is_html": True,
        "is_published": True,
        "cover": "recipes/covers/2023/01/01/bobo-de-camarao.webp",
        "category": "",
        "author": "",
    },
    {
        "title": "Picanha ao Forno com Sal Grosso",
        "description": (
            "A picanha ao forno com sal grosso é uma opção suculenta e cheia de sabor para os amantes de carne. "
            "A picanha ao forno com sal grosso é perfeita para um churrasco em casa ou para uma ocasião especial. "
            "Sirva com acompanhamentos como arroz, batatas ou uma salada fresca. "
            "Siga os passos dessa receita e desfrute de uma picanha ao forno saborosa e irresistível!"
        ),
        "slug": "picanha-ao-forno-com-sal-grosso",
        "preparation_time": 2,
        "preparation_time_unit": "Horas",
        "servings": 5,
        "servings_unit": "Porções",
        "preparation_steps": """
        1 - Cubra o fundo de uma assadeira com 1 kg do sal grosso. Coloque a picanha com a parte da gordura virada para cima. Cubra a carne
        com o restante do sal, não deixando nenhuma parte da carne exposta. Leve a assadeira para o forno a 200 graus.
        Retire a camada do sal e corte em fatias colocando o molho sobre a carne.

        2 - Dica: a picanha pode ser colocada para assar congelada.

        3 - Modo de Preparo do molho:
        Aqueça a manteiga junto com o azeite em uma frigideira, frite a cebola por alguns instantes e derrame sobre a picanha preparada.

        4 - Bom Apetite !!!
        """,
        "preparation_steps_is_html": False,
        "is_published": True,
        "cover": "recipes/covers/2023/01/01/picanha-no-forno-scaled.webp",
        "category": "",
        "author": "",
    },
    {
        "title": "Bolinho de chuva",
        "description": (
            "O bolinho de chuva doce é um petisco delicioso para todas as idades! "
            "Com gostinho de casa de vó, ele é perfeito para o lanche da tarde, "
            "acompanhado de um café quentinho. Confira agora mesmo como fazer bolinho de chuva simples!"
        ),
        "slug": "bolinho-de-chuva",
        "preparation_time": 30,
        "preparation_time_unit": "Minutos",
        "servings": 20,
        "servings_unit": "Unidades",
        "preparation_steps": """
            1 - Em um recipiente, adicione os ovos, o açúcar, o leite, a farinha de trigo e o fermento, depois misture-os até obter uma
            massa lisa e homogênea.

            2 - Com a ajuda de uma colher, pegue porções da mistura e despeje em uma panela com o óleo quente.

            3 - Retire do fogo quando estiver no ponto, depois misture a canela com açúcar e salpique no bolinho de chuva já frito.
        """,
        "preparation_steps_is_html": False,
        "is_published": True,
        "cover": "recipes/covers/2023/01/01/vovo-palmirinha-bolinho-de-chuva.jpg",
        "category": "",
        "author": "",
    },
]


if __name__ == "__main__":
    from pprint import pprint

    pprint(make_recipe())
