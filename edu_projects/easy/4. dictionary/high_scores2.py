# Рекорды 2.0
# Демонстрирует вложенные последовательности

scores = []

choice = None
while choice != "0":

    print(
    """
    Рекорды 2.0
    
    0 - Выйти
    1 - Показать рекорды
    2 - Добавить рекорды
    """
    )
    
    choice = input("Ваш выбор: ")
    print()

    # exit
    if choice == "0":
        print("Пока.")

    # display high-score table
    elif choice == "1":
        print("Рекорды\n")
        print("ИМЯ\tСЧЁТ")
        for entry in scores:
            score, name = entry    
            print(name, "\t\t", score)
        print(scores)

    # add a score
    elif choice == "2":
        name = input("Впишите имя игрока?: ")
        score = int(input("Bпишитe его результат?: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]    # в списке остается только 5 рекордов

    # непонятный пользовательский ввод
    else:
        print("Извините. в меню нет пункта", choice)
  
input("\n\nHaжмитe Enter, чтобы выйти.")
