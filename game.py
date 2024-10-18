from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import randrange

window = Tk()
window.title('Крестики and Нолики')
window.geometry('340x340')

frame = Frame(
    window,
    padx=10,
    pady=10
)

frame.pack(expand=True)

canvas = Canvas(bg="white", width=340, height=340)
canvas.pack(anchor=CENTER, expand=1)


def start_game():
    class Button:
        """ class for create/change button """

        def __init__(self, k, t):
            self.btn = ttk.Button(text=".", command=self.click_button)
            canvas.create_window(k, t, anchor=NW, window=self.btn, width=100, height=100)
            self.value = '.'

        def __bool__(self):
            return self.value == '.'

        def click_button(self, value='X'):
            """ Command click in button """
            if self.btn['text'] == '.':
                self.btn['text'] = value
                self.value = value

                self.check_win_and_next_move(value)

        def check_win_and_next_move(self, value):
            if check_win(value) == 'ok':
                start_game()
            else:
                if value == 'X':
                    random_pk()

    def random_pk():
        """ click computer random place """
        if check_tie():
            k = pole[randrange(0, 3)][randrange(0, 3)]
            while not k:
                k = pole[randrange(0, 3)][randrange(0, 3)]
            k.click_button('O')

    def check_tie():
        """ check tie """
        if not any(i.value == '.' for j in pole for i in j):
            messagebox.showinfo('bmi-pythonguides', 'НИЧЬЯ  😱')
            start_game()
        else:
            return True

    def check_win(value):
        """ check win in pole """
        if any(all(i.value == value for i in pole[j]) for j in range(3)):
            return win_print(value)
        if any(all(pole[j][i].value == value for i in range(3)) for j in range(3)):
            return win_print(value)
        if all(pole[i][j].value == value for i in range(3) for j in range(3) if i == j):
            return win_print(value)
        if all(pole[i][j].value == value for i in range(3) for j in range(3) if i + j == 2):
            return win_print(value)

    def win_print(value):
        if value == 'X':
            return messagebox.showinfo('bmi-pythonguides', 'ВЫ ВЫИГРАЛИ 😍')
        else:
            return messagebox.showinfo('bmi-pythonguides', 'ВЫ ПРОИГРАЛИ 😥')

    pole = [[Button(20, 20), Button(120, 20), Button(220, 20)],
            [Button(20, 120), Button(120, 120), Button(220, 120)],
            [Button(20, 220), Button(120, 220), Button(220, 220)]]


start_game()
window.mainloop()
