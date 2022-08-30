"""
Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его опадать. Компьютер
сообщает игроку, сколько букв в слове, и дает пяtь попыток узнаtь, есtь ли какая-либо буква в слове, причем
программа может отвечаtь только «Да» и «Her». Вслед за тем игрок должен попробовать отгадать слово.

"""
import random

words = ["мама", "яблоко", "машина"]

word = random.choice(words)
attempts = 5


def check_word():
    user_word = input("Назовите слово целиком:")
    if user_word == word:
        print("Верно это слово", word)
        exit()
    else:
        print("Неверно, это слово", word)


print("Количество букв в загаданном слове:", len(word))

while attempts > 0:
    print("Осталось попыток", attempts)
    user_letter = input("Введите букву, а я скажу вам если ли она в слове:")
    print("Вы выбрали букву -", user_letter)
    attempts = attempts - 1
    if user_letter in word:
        print(user_letter, "присутствует в загаданном слове")
    else:
        print(user_letter, "отсутствует в загаданном слове")
    user_choice = input("Хотите назвать слово целиком?\nВведите 'да' если хотите либо нажмите Enter если не хотите:")
    if user_choice == 'да':
        check_word()

print("Итак, попытки закончились")
check_word()
