import tkinter
from tkinter import *
from PIL import Image, ImageTk
import random
from random import randint

def Main_Window():
    root = Tk()
    root.title("")
    root.geometry("440x330+100+200")

    background_image = Image.open(r"C:\Users\Alisa\OneDrive\Desktop\CE ka data\Background.png")
    background_image = background_image.resize((440, 330), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(background_image)
    background_label = Label(root, image=background_image)
    background_label.place(x=0, y=0,width=440, height=330)

    Start_Button = Button(root,command=Start, text="Start", font=("times new roman", 25), bg="#FF0000", fg="white")
    Start_Button.place(x=110, y=130, width=200, height=50)

    Instruction_Button = Button(root,command=Instruction, text="Rules", font=("times new roman", 25), bg="#FF0000", fg="white")
    Instruction_Button.place(x=110, y=190, width=200, height=50)

    Exit_Button = Button(root,command=root.destroy, text="Exit", font=("times new roman", 25), bg="#FF0000", fg="white")
    Exit_Button.place(x=110, y=250, width=200, height=50)

    root.mainloop()

def Start():
    root = Tk()
    root.title("")
    root.geometry("490x350+100+200")

    title_lbl = Label(root, text="Rock, Paper, Scissor Game", font=("Bradley Hand ITC", 25, "bold"), bg="#DB7093", fg="#800080")
    title_lbl.place(x=0, y=0, width=490, height=45)

    Rock_img = "🪨"
    Paper_img = "📄"
    Scissor_img = "     ✂️"

    Player = Label(root, relief="solid", bd=3, text=Rock_img, font=("Bradley Hand ITC", 35, "bold"), bg="white", fg="Black")
    Player.place(x=6, y=110, width=120, height=110)
    Computer = Label(root, relief="solid", bd=3, text=Rock_img, font=("Bradley Hand ITC", 35, "bold"), bg="white", fg="Black")
    Computer.place(x=360, y=110, width=120, height=110)

    Player_Score = Label(root, relief="groove", bd=5, text="0", font=("times new roman", 25, "bold"), bg="white", fg="Black")
    Player_Score.place(x=140, y=130, width=70, height=70)
    Computer_Score = Label(root, relief="groove", bd=5, text="0", font=("times new roman", 25, "bold"), bg="white", fg="Black")
    Computer_Score.place(x=275, y=130, width=70, height=70)

    Player_indicator = Label(root, text="Player", font=("Bradley Hand ITC", 25, "bold"), bg="#4682B4", fg="Black")
    Player_indicator.place(x=6, y=53, width=150, height=47)
    Computer_indicator = Label(root, text="Computer", font=("Bradley Hand ITC", 25, "bold"), bg="#4682B4", fg="Black")
    Computer_indicator.place(x=330, y=53, width=150, height=45)

    Final_Message = Label(root, relief="ridge", bd=7, text="Good Luck!!", font=("Bradley Hand ITC", 25, "bold"), bg="black", fg="red")
    Final_Message.place(x=110, y=288, width=260, height=52)

    Button_rock = Button(root, relief="raised", bd=4, command=lambda: choice_update("rock"), text="Rock", font=("times new roman", 22), bg="gray", fg="white")
    Button_rock.place(x=10, y=230, width=150, height=50)

    Paper_Button = Button(root, relief="raised", bd=4, command=lambda: choice_update("paper"), text="Paper", font=("times new roman", 22), bg="gray", fg="white")
    Paper_Button.place(x=170, y=230, width=150, height=50)

    Button_Scissor = Button(root, relief="raised", bd=4, command=lambda: choice_update("scissor"), text="Scissor", font=("times new roman", 22), bg="gray", fg="white")
    Button_Scissor.place(x=330, y=230, width=150, height=50)

    def msg_Updation(a):
        Final_Message["text"] = a

    def Computer_Update():
        final = int(Computer_Score["text"])
        final += 1
        Computer_Score["text"] = str(final)

    def Player_Update():
        final = int(Player_Score["text"])
        final += 1
        Player_Score["text"] = str(final)

    def winner_check(p, c):
        if p == c:
            msg_Updation("It's a tie")
        elif p == "rock":
            if c == "paper":
                msg_Updation("Computer Wins!!")
                Computer_Update()
            else:
                msg_Updation("Player Wins!!")
                Player_Update()
        elif p == "paper":
            if c == "scissor":
                msg_Updation("Computer Wins!!")
                Computer_Update()
            else:
                msg_Updation("Player Wins!!")
                Player_Update()
        elif p == "scissor":
            if c == "rock":
                msg_Updation("Computer Wins!!")
                Computer_Update()
            else:
                msg_Updation("Player Wins!!")
                Player_Update()
        else:
            pass
    to_select = ["rock", "paper", "scissor"]

    def choice_update(a):
        choice_computer = to_select[random.randint(0, 2)]
        if choice_computer == "rock":
            Computer["text"] = Rock_img
        elif choice_computer == "paper":
            Computer["text"] = Paper_img
        elif choice_computer == "scissor":
            Computer["text"] = Scissor_img

        if a == "rock":
            Player["text"] = Rock_img
        elif a == "paper":
            Player["text"] = Paper_img
        else:
            Player["text"] = Scissor_img

        winner_check(a, choice_computer)

    root.mainloop()

def Instruction():
    root = Tk()
    root.title("")
    root.geometry("580x350+100+200")

    title_lbl = Label(root, text="INSTRUCTIONS", font=("Bradley Hand ITC", 25, "bold"), bg="gray",fg="Black")
    title_lbl.place(x=0, y=0, width=580, height=45)
    Welcome="  Welcome to Rock-Paper-Scissors Game!"
    Instruction="How to Play:\n 1. Each player have three options: Rock, Paper,or Scissors\n2. Rock beats Scissors ,Scissors beats Paper\nPaper beats Rock\n" \
                "3. The player who wins the round gets a point.\n4. The scores of both the player and computer will be\nupdated accordingly."
    End=" Have fun and enjoy the game!"
    title_lbl = Label(root, text=Welcome, font=("Bradley Hand ITC", 18, "bold"), fg="Black")
    title_lbl.place(x=0, y=55, width=520, height=50)

    title_lbl = Label(root, text=Instruction, font=("times new roman", 18, ), fg="Black")
    title_lbl.place(x=0, y=88, width=580, height=230)

    title_lbl = Label(root, text=End, font=("Bradley Hand ITC", 18,"bold"), fg="Black")
    title_lbl.place(x=0, y=299, width=570, height=50)
    root.mainloop()

Main_Window()
