# Компьютерный датчик настроения
# Демонстрирует использование elif

import random

print("Я ощущаю вашу энергетику. От моего экрана не скрыто ни одно из ваших чувств.")
print("Итaк. ваше настроение ... ")

mood = random.randint(1, 3)

if mood == 1:
    # happy
    print(
        """
           -----------
           |         |
           | O    O  |
           |   <     |
           |         |
           | .     . |
           |  `...`  |
           -----------
                       """)
elif mood == 2:
    # neutral  
    print(
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | ------  |
       |         |
       -----------
                   """)
elif mood == 3:
    # sad
    print(
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       |  .'.    |
       | '   '   |
       -----------
                   """)
else:
    print("He бывает такого настроения! (Должно быть. вы совершенно не в себе.)")

print(" ... Но это только сегодня. ")

input("\n\nHaжмитe Enter. чтобы выйти.")







