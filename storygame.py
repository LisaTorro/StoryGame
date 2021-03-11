# Created by Lisa Torro
# V1 3/10/21
# This is unfinished and simply brings up a GUI with a lable and two buttons that don't function.
# Next step is to get buttons to go to a new page (start the game)

import tkinter
import tkinter.font


def main():
    window = tkinter.Tk()
    window.geometry("800x500")
    window.configure(bg="#fcf3f4")
    fontSize1 = tkinter.font.Font(size=25)
    frm_1 = tkinter.Frame(relief=tkinter.RIDGE, borderwidth=5)
    greeting = tkinter.Label(
        master=frm_1,
        text="Welcome to the game! Choose a story genre.",
        bg="#fcdedf"
    )
    greeting['font'] = fontSize1
    greeting.pack()

    frm_2 = tkinter.Frame()

    fantasy = tkinter.Button(
        master=frm_2,
        text="Fantasy",
        width=25,
        height=5,
        bg="tan",
        fg="brown",
        activebackground="gray"
    )
    fantasy.pack()

    frm_3 = tkinter.Frame()
    action = tkinter.Button(
        master=frm_3,
        text="Action",
        width=25,
        height=5,
        bg="red",
        fg="blue",
        activebackground="gray"
    )
    action.pack()

    frm_1.pack()
    frm_2.pack(padx=10, pady=10)
    frm_3.pack()
    window.mainloop()


main()
