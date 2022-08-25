import random

hp_player = 100
eaten_pies = 0

while hp_player > 0 and eaten_pies != 5:
    random_number = random.randint(1, 4)
    print("Ваше здоровье", hp_player)
    print("Съедено пирожков", eaten_pies)
    input("ВЫ играете в пирожок с сюрпризом,\nнажмите энтэр чтобы узнать с какой начинкой пирожок:>")
    eaten_pies = eaten_pies + 1
    if random_number == 1:
        print("Вам попался пирожок с мясом")
        hp_player = min(hp_player, hp_player+10)
        print("Вы пополнили здоровье на 10")
    if random_number == 2:
        print("Вам попался пирожок с газом")
        hp_player = hp_player - 25
        print("Вы отравились газом, ваше здоровье уменьшилось на 25")
    if random_number == 3:
        print("Вам попался пирожок с золотом")
        hp_player = min(hp_player, hp_player + 25)
        print("Вы пополнили здоровье на 25")
    if random_number == 4:
        print("Вам попался пирожок с молотом")
        hp_player = hp_player - 15
        print("Вы подавились молотом, ваше здоровье уменьшилось на 15")
    print("\n______________________")
if eaten_pies == 5:
    print("Вы выжили победа!")
else:
    print("Вы отравились пирожками... пока")

