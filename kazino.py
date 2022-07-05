from tkinter import *
import time
import threading
import random
from tkinter import messagebox as mb

gray="#3C3F41"
white="#FFFFFF"

rt_text="0"

anim=0
num1=0
num=0

balance=1

def is_anim(event):
    global anim,balance,num
    try:
        num = int(entr.get())
        if balance >= 1 and num >=0 and num <=9:
            anim=1
            label_balance["text"]="Ваш баланс: {}".format(balance)
        if num >= 10:
            mb.showerror("Ошибка", "Введите число от 0 до 9")
        if balance <=0:
            mb.showerror("Ошибка", "Недостаточно денег на балансе")
    except ValueError:
        mb.showerror("Ошибка", "Введите число")

def animation():
    global anim,move_pos,balance,num1

    while True:
        if anim == 0:
            continue

        if anim == 1:
            num = int(entr.get())
            if num == "":
                mb.showerror("Ошибка", "Введите число")
            if num >= 10:
                mb.showerror("Ошибка", "Введите число от 0 до 9")


            balance-=1
            label_balance["text"] = "Ваш баланс: {}".format(balance)
            but_place["state"] = "disabled"

            for i in range(5):

                num1 = random.randint(0, 9)

                rt1["text"] = num1
                rt2["text"] = num1
                rt3["text"] = num1
                time.sleep(0.2)

            if num == num1:
                mb.showinfo("Информация","Вы выиграли!")
                balance+=10
                label_balance["text"]="Ваш баланс: {}".format(balance)
            if num != num1:
                mb.showinfo("Информация","Вы проиграли!")
                label_balance["text"]="Ваш баланс: {}".format(balance)

            anim=0
            but_place["state"] = "normal"

root=Tk()

root.geometry("400x400")
root["bg"]=gray
root.title("Казино")

label_balance=Label(root,text="Ваш баланс: {}".format(balance),font="Arial 20",bg=gray,fg=white)
label_balance.place(x=10,y=350)

lab=Label(root,text="Выберите число",font="Arial 35",bg=gray,fg=white)
lab.place(x=20,y=20)

rt1=Label(root,text=rt_text,font="Arial 40",bg=gray,fg=white)
rt2=Label(root,text=rt_text,font="Arial 50",bg=gray,fg=white)
rt3=Label(root,text=rt_text,font="Arial 40",bg=gray,fg=white)

rt1.place(x=0+120,y=105-15)
rt2.place(x=60+120,y=110-15)
rt3.place(x=120+120,y=105-15)

entr=Entry(root,width=15,font="Arial 20")
entr.place(x=90,y=200)

but_place=Button(root,text="Поставить",font="Arial 25",bg=gray,fg=white)
but_place.place(x=110,y=250)
but_place.bind("<Button-1>",is_anim)

threading.Thread(target=animation).start()

root.mainloop()