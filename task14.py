from tkinter import *
top=Tk()
top.title("COFFEE MACHINE")
L=Label(top,text="COFFEE MACHINE",font=("Echelon",22),fg="red").place(x=260,y=60)
top.geometry("960x720")
l1=Label(top,text="WELCOME",font=("BAZOOKA",22),fg="red")
l2=Label(top,text="What Would You Like?",font=("Echelon",20),fg="darkgreen").place(x=69,y=118)
bt1=Button(top,text="LATTE",font=("Halston",12),fg="navy").place(x=300,y=160)
bt2=Button(top,text="ESPREESO",font=("Halston",12),fg="navy").place(x=450,y=160)
bt3=Button(top,text="CAPPUCCINO",font=("Halston",12),fg="navy").place(x=600,y=160)
bt4=Button(top,text="OFF",font=("Halston",12),fg="black").place(x=750,y=160)
n1=StringVar()
n2=StringVar()
n3=StringVar()
n4=StringVar()
l3=Label(top,text="How Many Conis?",font=("Echelon",16),fg="Maroon").place(x=64,y=200)
la1=Label(top,text="How Many Quarters?",font=("Halston",12),fg="black").place(x=64,y=230)
la2=Label(top,text="How Many Dimes?",font=("Halston",12),fg="black").place(x=64,y=280)
la3=Label(top,text="How Many Nickles?",font=("Halston",12),fg="black").place(x=64,y=330)
la4=Label(top,text="How Many Pennies?",font=("Halston",12),fg="black").place(x=64,y=375)
a1=Spinbox(top,from_=0,to =100).place(x=250,y=230)
a2=Spinbox(top,from_=0,to =100).place(x=250,y=280)
a3=Spinbox(top,from_=0,to =100).place(x=250,y=330)
a4=Spinbox(top,from_=0,to =100).place(x=250,y=380)
bt5=Button(top,text="ENTER", font=(12),fg="indigo").place(x=250,y=600)
bt6=Button(top,text="CANCEL", font=(12),fg="indigo").place(x=350,y=600)
top.mainloop()           
           


                                            

             
