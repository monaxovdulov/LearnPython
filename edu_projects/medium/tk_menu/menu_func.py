import tkinter

main = tkinter.Tk()

mframe = tkinter.Frame(main)
mframe.pack()


def clearwin():
    '''Clear the main windows frame of all widgets'''
    for child in mframe.winfo_children():
        child.destroy()


def main_menu():
    '''Create the main window'''
    clearwin()
    b1 = tkinter.Button(mframe, command=win2, text='Начать игру')
    b1.pack()
    b2 = tkinter.Button(mframe, command=win3, text='об игре')
    b2.pack()


def win2():
    '''Create the second sub window'''
    clearwin()
    entry1 = tkinter.Entry(mframe)
    entry1.pack()
    back = tkinter.Button(mframe, command=main_menu, text='Назад')
    back.pack()


def win3():
    '''Create the third sub window'''
    clearwin()
    label1 = tkinter.Label(mframe, text='This is the third window!')
    label1.pack()
    back = tkinter.Button(mframe, command=main_menu, text='Назад')
    back.pack()


main_menu()

main.mainloop()
