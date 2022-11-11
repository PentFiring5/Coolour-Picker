from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Colour Picker")
root.geometry("400x130")
#root.iconbitmap('test2.ico')


# test =11111
# f"blablan {test} hadfiwfhd"

def colour():
    global my_Lable
    clicked = StringVar()
    # time2 = 3000

    my_colour = colorchooser.askcolor()
    my_Lable = Label(root,text= my_colour , bg=my_colour[1])         # displays in this {R,G,B} #0w0w0w order
    # my_Lable = Label(root, text= f"RGB→ {my_colour} ←HEX", bg=my_colour[1])            displays in this RGB→ ((R,G,B)'#0w0w0w') ←HEX order
    my_Lable.place(x=110,y=55)
    # my_Lable2 = Label(root, text="Gewählt", font=("Helvetica", 32), bg=my_colour)
    # my_Lable2.pack()

    # clear= Button(root,text="Clear", command=kill)
    # clear.place(x=83, y=5)

    clicked.set("HEX oder RGB Kopieren")
    coppy = OptionMenu(root, clicked, "RGB Kopieren", "HEX Kopieren")
    coppy.place(x=123,y= 3)

    def Suche21():
        # clicked.set("HEX oder RGB Kopieren")
        time2 = 4000
        HEX = "HEX Kopieren"
        RGB = "RGB Kopieren"

        if clicked.get() == RGB:
            root.clipboard_clear()
            root.clipboard_append(my_colour[0])

            top = Tk()
            top.title("RGB Code Kopiert !!!")
            top.geometry("300x50")
            #top.iconbitmap('test2.ico')
            info = Label(top, text=" RGB Code Kopiert !!!")
            info.pack()
            clicked.set("HEX oder RGB Kopieren")
            top.after(time2, lambda: top.destroy())
            top.mainloop()

        if clicked.get() == HEX:
            root.clipboard_clear()
            root.clipboard_append(my_colour[1])

            top = Tk()
            top.title("Hex Code Kopiert !!!")
            top.geometry("300x50")
            #top.iconbitmap('test2.ico')
            info = Label(top, text=" HEX Code Kopiert !!!")
            info.pack()
            clicked.set("HEX oder RGB Kopieren")
            top.after(time2, lambda: top.destroy())
            top.mainloop()

    KopyButton = Button(root, text="Kopieren", command=Suche21)
    KopyButton.place(x=180, y=90)

def kill():
    my_Lable.destroy()

my_Button = Button(root, text="Suche Farbe aus", command=colour)
my_Button.place(x=296,y=5)

exit_Button = Button(root, text="Abbrechen",bg="#dc5432", fg="black", command=root.destroy)
exit_Button.place(x= 8, y= 5)
#dc5432
clear= Button(root,text="Clear", command=kill)
clear.place(x=83, y=5)

root.mainloop()
