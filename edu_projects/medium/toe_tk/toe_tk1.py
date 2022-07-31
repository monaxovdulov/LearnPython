from tkinter import *
"""По мере написания игры изучим метод config,
глобальные и локальные переменные, метод grid, lambda функции."""
root = Tk()
root.title('🍌🍌')
count = 0

def b_click(b):
    b["text"] = "X"


color = "grey"

b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg=color,
            command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg=color)
b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg=color)
b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg=color)
b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg=color)
b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg=color)
b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg=color)
b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg=color)
b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg=color)

# Grid our buttons to the screen
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

root.mainloop()
