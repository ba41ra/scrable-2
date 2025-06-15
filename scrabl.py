import random

LETTER_SCORES = {
    "А": 1,
    "Б": 3,
    "В": 4,
    "Г": 2,
    "Д": 3,
    "Е": 1,
    "Ё": 5,
    "Ж": 4,
    "З": 3,
    "И": 1,
    "Й": 7,
    "К": 2,
    "Л": 3,
    "М": 2,
    "Н": 4,
    "О": 1,
    "П": 3,
    "Р": 4,
    "С": 3,
    "Т": 5,
    "У": 2,
    "Ф": 8,
    "Х": 6,
    "Ц": 7,
    "Ч": 4,
    "Ш": 8,
    "Щ": 9,
    "Ъ": 10,
    "Ы": 3,
    "Ь": 6,
    "Э": 5,
    "Ю": 3,
    "Я": 4
}


def get_random_letter():
    converted_dictionary = list(LETTER_SCORES.keys())
    random_letter = random.choice(converted_dictionary)
    return random_letter


def get_word_with_letter(letter):
    while True:
        word = input(f'Введите слова на букву "{letter}": ')
        if letter == word[0].upper():
            break
        print(f"Слово не на букву: {letter}, попробуйте заново.")
    return word


def calculate_score(word):
    all_scores = []
    for symbol in word.upper():
        scores = LETTER_SCORES.get(symbol)
        all_scores.append(scores)
    sum_scores = sum(all_scores)
    return sum_scores


def main():
    rand_letter = get_random_letter()
    print("Начальная буква:", rand_letter)
    print("Игрок 1")
    word_1 = get_word_with_letter(rand_letter)
    player_score_1 = calculate_score(word_1)
    print("Игрок 2")
    word_2 = get_word_with_letter(rand_letter)
    player_score_2 = calculate_score(word_2)
    print(f"Игрок 1 ввел слово {word_1}, и получил {player_score_1} очков")
    print(f"Игрок 1 ввел слово {word_2}, и получил {player_score_2} очков")
    if player_score_1 > player_score_2:
        print("Игрок 1 победил")
    elif player_score_1 < player_score_2:
        print("Игрок 2 победил")
    else:
        print("Ничья")


if __name__ == '__main__':
    main()
