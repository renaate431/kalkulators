import re
from tkinter import*
mansLogs=Tk() #saiisinājums tkinker
mansLogs.title("+-*/=calc")# iedod nosaukumu
#mansLogs.geometry("300x400")# loga izmērs, kalkulatora izmērs
#poga=Button(mansLogs, text="hey!", bg="green", fg="white") #bg -background fg=priekšplāna krāsa
#pack- parādīt
#poga.pack()
e=Entry(mansLogs,width=15, font=("Arial Black",20), bg=("black"), fg=("white"))
e.grid(row=0,column=0,columnspan=4)


def btnClick(number):
    current=e.get()#nolasa esošo skaitli
    e.delete(0,END)#nodzēš
    newNumber=str(current)+str(number)
    e.insert(0,newNumber)# ievieto displejā
    return 0


#-------------------------------------------------------------------------
def btnCommand(command):
    global num1 #jāiegaumē skaitlis un darbība
    global mathOp #matemātikas operators
    mathOp=  command #+,-,*,/
    num1= int(e.get())
    e.delete(0,END)
    return 0

 #----------------------------------------------------------------------   

def equal(command):
    global num2
    num2=(int(e.get()))
    result=0
    if mathOp=="-":
        result=num1-num2
    elif mathOp=="+":
        result= num1+num2
    elif mathOp=="*":
        result= num1*num2
    elif mathOp=="/":
        result=num1/num2
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0

#-----------------------------------------------------------------------------------
def clear(command):
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0

#------------------------------------------------------------------------------------



btn0=Button(mansLogs, text="0 ", padx="40", pady="20", command=lambda:btnClick(0),bg="black", fg="hot pink")# funkcija 
btn1=Button(mansLogs, text="1 ", padx="40", pady="20", command=lambda:btnClick(1),bg="black", fg="hot pink")
btn2=Button(mansLogs, text="2 ", padx="40", pady="20", command=lambda:btnClick(2),bg="black", fg="hot pink")
btn3=Button(mansLogs, text="3 ", padx="40", pady="20", command=lambda:btnClick(3),bg="black", fg="hot pink")
btn4=Button(mansLogs, text="4 ", padx="40", pady="20", command=lambda:btnClick(4),bg="black", fg="hot pink")
btn5=Button(mansLogs, text="5 ", padx="40", pady="20", command=lambda:btnClick(5),bg="black", fg="hot pink")
btn6=Button(mansLogs, text="6 ", padx="40", pady="20", command=lambda:btnClick(6),bg="black", fg="hot pink")
btn7=Button(mansLogs, text="7 ", padx="40", pady="20", command=lambda:btnClick(7),bg="black", fg="hot pink")
btn8=Button(mansLogs, text="8 ", padx="40", pady="20", command=lambda:btnClick(8),bg="black", fg="hot pink")
btn9=Button(mansLogs, text="9 ", padx="40", pady="20", command=lambda:btnClick(9),bg="black", fg="hot pink")
btn10=Button(mansLogs,text="/ ", padx="40", pady="20", command=lambda:btnCommand("/"),bg="black", fg="hot pink")
btn11=Button(mansLogs,text="* ", padx="40", pady="20", command=lambda:btnCommand("*"),bg="black", fg="hot pink")
btn12=Button(mansLogs,text="+ ", padx="40", pady="20", command=lambda:btnCommand("+"),bg="black", fg="hot pink")
btn13=Button(mansLogs,text="- ", padx="40", pady="20", command=lambda:btnCommand("-"),bg="black", fg="hot pink")
btn14=Button(mansLogs,text="= ", padx="40", pady="20",bg="black", fg="hot pink", command=lambda:equal("="))
btn15=Button(mansLogs,text="C",padx="40", pady="20",bg="black", fg="hot pink", command=lambda:clear("C"))



btn0.grid(row=4,column=1)
btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)
btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)
btn15.grid(row=4,column=0)
btn10.grid(row=1,column=3)
btn11.grid(row=2,column=3)
btn13.grid(row=4,column=3)
btn12.grid(row=3,column=3)
btn14.grid(row=4,column=2)













mansLogs.mainloop()# šis ir obligāti! paliek pašā apakšā. Viss ko tu darīsi saglabāsi un palaidīsi, šī funkcija parādīs tās jaunās lietas