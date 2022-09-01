import random
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("rock, paper, scissors, lizard, spock")


def comp_aw_label(computer):
    global Label_r
    global Label_p
    global Label_s
    global Label_x
    global Label_v
    Label_r.grid_forget()
    Label_p.grid_forget()
    Label_s.grid_forget()
    Label_x.grid_forget()
    Label_v.grid_forget()
    if computer == "r":
        Label_r = Label(root, image=rock_img)
        Label_r.grid(row=0, columnspan=5)
    elif computer == "p":
        Label_p = Label(root, image=paper_img)
        Label_p.grid(row=0, columnspan=5)
    elif computer == "s":
        Label_s = Label(root, image=scissors_img)
        Label_s.grid(row=0, columnspan=5)
    elif computer == "x":
        Label_s = Label(root, image=lizard_img)
        Label_s.grid(row=0, columnspan=5)
    elif computer == "v":
        Label_s = Label(root, image=vulcan_img)
        Label_s.grid(row=0, columnspan=5)
    else:       # nur bei Fehler
        Label_r.grid_forget()
        Label_p.grid_forget()
        Label_s.grid_forget()
        Label_x.grid_forget()
        Label_v.grid_forget()


# 1: s > p , 2: p > r , 3: r > x , 4: x > v, 5: v > s, 6: s > x , 7: x > p , 8: p > v , 9: v > r , 10: r > s
def is_win(player, comp):
    if (player == "s" and comp == "p") or (player == "p" and comp == "r") or (player == "r" and comp == "x") or (player == "x" and comp == "v") or (player == "v" and comp == "s") or (player == "s" and comp == "x") or (player == "x" and comp == "p") or (player == "p" and comp == "v") or (player == "v" and comp == "r") or (player == "r" and comp == "s"):
        return True


def play(user):
    global Label_text
    computer = random.choice(["r", "p", "s", "x", "v"])

    comp_aw_label(computer)

    if user == computer:
        Label_text.grid_forget()
        Label_text = Label(root, text="\ntie!\n")
        Label_text.grid(row=1, columnspan=5)

    elif is_win(user, computer):
        Label_text.grid_forget()
        Label_text = Label(root, text="\nYou won!\n")
        Label_text.grid(row=1, columnspan=5)

    else:
        Label_text.grid_forget()
        Label_text = Label(root, text="\nYou lost.\n")
        Label_text.grid(row=1, columnspan=5)




# Bild importieren und in Var speichern
rock_img = ImageTk.PhotoImage(Image.open("Py_images/rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("Py_images/paper.png"))
scissors_img = ImageTk.PhotoImage(Image.open("Py_images/scissors.png"))
lizard_img = ImageTk.PhotoImage(Image.open("Py_images/lizard.png"))
vulcan_img = ImageTk.PhotoImage(Image.open("Py_images/vulcan.png"))

Label_r = Label(root, image=rock_img)
Label_p = Label(root, image=paper_img)
Label_s = Label(root, image=scissors_img)
Label_x = Label(root, image=lizard_img)
Label_v = Label(root, image=vulcan_img)

Label_r.grid(row=0, column=0)
Label_p.grid(row=0, column=1)
Label_s.grid(row=0, column=2)
Label_x.grid(row=0, column=3)
Label_v.grid(row=0, column=4)

Label_text = Label(root, text="\nMake your choice!\n")
Label_text.grid(row=1, columnspan=5)

Button_r = Button(root, image=rock_img, command=lambda: play("r"))
Button_p = Button(root, image=paper_img, command=lambda: play("p"))
Button_s = Button(root, image=scissors_img, command=lambda: play("s"))
Button_x = Button(root, image=lizard_img, command=lambda: play("x"))
Button_v = Button(root, image=vulcan_img, command=lambda: play("v"))

Button_r.grid(row=3, column=0)
Button_p.grid(row=3, column=1)
Button_s.grid(row=3, column=2)
Button_x.grid(row=3, column=3)
Button_v.grid(row=3, column=4)

root.mainloop()
