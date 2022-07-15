import random
import numpy as np


alphabet = {
    1: "א",
    2: "ב",
    3: "ג",
    4: "ד",
    5: "ה",
    6: "ו",
    7: "ז",
    8: "ח",
    9: "ט",
    10: "י",
    11: "כ",
    12: "ל",
    13: "מ",
    14: "נ",
    15: "ס",
    16: "ע",
    17: "פ",
    18: "צ",
    19: "ק",
    20: "ר",
    21: "ש",
    22: "ת"
}


title = {
    1: "Алеф",
    2: "бэт",
    3: "гИмэль",
    4: "дАлет",
    5: "hэй",
    6: "вав",
    7: "зайн",
    8: "хэт",
    9: "тэт",
    10: "йуд",
    11: "каф",
    12: "лАмед",
    13: "мэм",
    14: "нун",
    15: "сАмэх",
    16: "айн",
    17: "пэй",
    18: "цАди",
    19: "куф",
    20: "рэш",
    21: "шин",
    22: "тав",
}


pronunciation = {
    1: "нет",
    2: "Б или В",
    3: "Г",
    4: "Д",
    5: "h",
    6: "О или И или В",
    7: "З",
    8: "Х",
    9: "Т",
    10: "Й или И",
    11: "К или Х",
    12: "Л",
    13: "М",
    14: "Н",
    15: "С",
    16: "нет",
    17: "П или Ф",
    18: "Ц",
    20: "Р",
    21: "Ш или C",
    22: "Т",
}


def learning_title():
    """
    Learning the names of the hebrew letters
    """
    num = np.random.randint(1, 22)
    letter = alphabet[num]
    print(f"Что это за буква? {letter}")
    input_title = input().strip()
    if title[num].lower() == input_title.lower():
        print(f"Верно! Это буква '{title[num]}'")
        print()
    else:
        print(f"Нет, это буква называется '{title[num]}'")
        print()


def learning_pronunciation():
    """
    Learning the pronunciation of the hebrew letters
    """
    num = random.randint(1, 22)
    letter = alphabet[num]
    print(f"Как произносится эта буква? {letter}")
    input_pronunciation = input().strip()
    if pronunciation[num].lower() == input_pronunciation.lower():
        print(f"Верно! Это буква '{title[num]}'. Она произноится '{pronunciation[num]}'")
        print()
    else:
        print(f"Нет. Это буква '{title[num]}'. Она произноится '{pronunciation[num]}'")
        print()


game = {
    1: learning_title,
    2: learning_pronunciation
}


def play_or_stop():
    """
    Continue playing game or not
    """
    print(f"Введи 'да', если хочешь еще. Иначе введи 'нет'")
    more_or_break = input().lower().strip()
    if more_or_break == "нет":
        print("Конец игры")
        return False
    elif more_or_break == "да":
        print()
        return True
    else:
        print(f"Ошибка ввода.")
        play_or_stop()


def main():
    print("Выбери номер игры:")
    print("1 - Учим названия букв")
    print("2 - Учим произношение букв", end="\n\n")
    num_game = int(input())
    while True:
        game[num_game]()
        what_to_do = play_or_stop()
        if what_to_do is False:
            break

    

if __name__ == "__main__":
    main()
