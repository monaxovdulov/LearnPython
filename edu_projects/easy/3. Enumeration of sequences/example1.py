# как цикл for работает с разными типами объектов


# оператор цикла for работает по разному с разными типами данных
data1 = ["Alex", "Misha", "Jack"]
data2 = "Hello"
data3 = {"Alex": 100, "Nadya": 100, "Mr. Pomidor": 100}
data4 = range(10)  # функция range создаст диапазон чисел: 0 1 2 3 4 5 6 7 8 9

print(data2)

for i in data4:
    print(i)