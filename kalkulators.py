from tkinter import*
mansLogs=Tk() #saiisinājums tkinker
mansLogs.title("kalkulators")# iedod nosaukumu
#mansLogs.geometry("300x400")# loga izmērs, kalkulatora izmērs
#poga=Button(mansLogs, text="hey!", bg="green", fg="white") #bg -background fg=priekšplāna krāsa
#pack- parādīt
#poga.pack()
btn0=Button(mansLogs, text="0", padx="40", pady="40")
btn1=Button(mansLogs, text="1", padx="40", pady="40")
btn2=Button(mansLogs, text="2", padx="40", pady="40")
btn3=Button(mansLogs, text="3", padx="40", pady="40")
btn4=Button(mansLogs, text="4", padx="40", pady="40")
btn5=Button(mansLogs, text="5", padx="40", pady="40")
btn6=Button(mansLogs, text="6", padx="40", pady="40")
btn7=Button(mansLogs, text="7", padx="40", pady="40")
btn8=Button(mansLogs, text="8", padx="40", pady="40")
btn9=Button(mansLogs, text="9", padx="40", pady="40")
btn10=Button(mansLogs,text="/", padx="40", pady="40")
btn11=Button(mansLogs,text="*", padx="40", pady="40")
btn12=Button(mansLogs,text="+", padx="40", pady="40")
btn13=Button(mansLogs,text="-", padx="40", pady="40")
btn14=Button(mansLogs,text="=", padx="40", pady="40")
btn15=Button(mansLogs,text="del",padx="40", pady="40")



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
btn12.grid(row=4,column=2)
btn15.grid(row=4,column=0)
btn10.grid(row=1,column=3)
btn11.grid(row=2,column=3)
btn13.grid(row=4,column=3)
btn12.grid(row=4,column=3)













mansLogs.mainloop()# šis ir obligāti! paliek pašā apakšā. Viss ko tu darīsi saglabāsi un palaidīsi, šī funkcija parādīs tās jaunās lietas