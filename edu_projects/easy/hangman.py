import random

HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")
MAX_WRONG = len(HANGMAN) - 1

WORDS = ("СТОЛОВАЯ", "РЕСТОРАН", "ШКОЛА", "СПРАВКА", "АНЕКДОТ", "ЗАВТРАК", "БИЗНЕС")
word = random.choice(WORDS)
so_far = "-" * len(word)

wrong = 0

used = []
print(word)
print("\t\tДобро пожаловать в игру 'Виселица'!")
print(HANGMAN[wrong])
print("\nОтгаданное вами в слове сейчас выглядит так:\n", so_far)
guess = input("\n\nВведите букву: ")
print("вы ввели букву", guess)
guess = guess.upper()

if guess in word:
    print("\nДа! Буква", guess, "есть в слове!")
    new = ""
