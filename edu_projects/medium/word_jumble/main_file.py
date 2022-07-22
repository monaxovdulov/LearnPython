# Анаграммы Word Jumble)
#
# Компьютер выбирает какое-пибо слово и хаотически переставляет его буквы
# Задача иrрока - восстановить исходное слово

import random

WORDS = []

f = open('words.txt', 'r', encoding='utf-8')
for word in f.readlines():
    WORDS.append(word.replace('\n', ''))
f.close()

print(WORDS)


# случайным образом выберем из последовательности одно слово
word = random.choice(WORDS)

# создадим переменную. с которой будет затем сопоставлена версия игрока
correct = word

# создадим анаграмму выбранного слова, в которой буквы будут расставлены хаотично
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble = jumble + word[position]
    word = word[:position] + word[(position + 1):]

# начало игры
print("""
        Добро пожаловать в игру 'Анаграммы'!
    Надо переставить буквы так. чтобы получилось осмысленное слово.
(Для выхода нажмите Enter, не вводя своей версии.
""")

print("Boт анаграмма:", jumble)

guess = input("\nПопробуйте отгадать исходное слово: ")
while guess != correct and guess != "":
    print("K сожалению. вы неправы.")
    guess = input("Попробуйте отгадать исходное слово: ")

if guess == correct:
    print("Дa. именно так! Вы отгадали!\n")

print("Спасибо за игру.")

input("\n\nHaжмитe Enter. чтобы выйти")
