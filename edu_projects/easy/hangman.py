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
while so_far != word and wrong < MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nОтгаданное вами в слове сейчас выглядит так:\n", so_far)
    guess = input("\n\nВведите букву: ")
    print("вы ввели букву", guess)
    guess = guess.upper()
    if guess in word:
        print("\nДа! Буква", guess, "есть в слове!")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new = new + guess
            else:
                new = new + so_far[i]
        so_far = new
    else:
        print("Ты ошибся!")
        wrong = wrong + 1
    print(so_far)
