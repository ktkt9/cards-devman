from faker import Faker
import file_operations
import random
import os
import glob


fake = Faker("ru_RU")

LETTERS_MAPPING = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}

SKILLS = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд"
]
OUTPUT_FOLDER = "cards"
NUM_CARDS = 10


def stylize_text(text):
    result = ""
    for letter in text:
        result += LETTERS_MAPPING.get(letter, letter)
    return result


def clean_old_cards(output_folder):
    old_cards = glob.glob(os.path.join(output_folder, "card_*.svg"))
    for old_card in old_cards:
        os.remove(old_card)


def generate_character_data():
    surname = fake.last_name()
    name = fake.first_name()
    job = fake.job()
    town = fake.city()
    
    strength, agility, endurance, intelligence, luck = [random.randint(3, 18) for _ in range(5)]
    
    skill = random.sample(SKILLS, 3)
    skill = [stylize_text(s) for s in skill]
    
    return {
        "first_name": name,
        "last_name": surname,
        "job": job,
        "town": town,
        "strength": strength,
        "agility": agility,
        "endurance": endurance,
        "intelligence": intelligence,
        "luck": luck,
        "skill_1": skill[0],
        "skill_2": skill[1],
        "skill_3": skill[2]
    }


def create_card(context, output_filename):
    file_operations.render_template("template.svg", output_filename, context)


def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    clean_old_cards(OUTPUT_FOLDER)

    for i in range(NUM_CARDS):
        context = generate_character_data()
        output_filename = os.path.join(OUTPUT_FOLDER, f"card_{i+1}.svg")
        
        create_card(context, output_filename)
        print(f"Создана карточка: {output_filename}")


if __name__ == '__main__':
    main()