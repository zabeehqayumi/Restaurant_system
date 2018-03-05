from tkinter import *
import random
import time;


root= Tk()
root.geometry("1600x800+0+0")
root.title("Developer: ZQ")

text_input = StringVar()
operator = ""



tops= Frame(root, width=1600, height= 50, bg= "powder blue", relief= SUNKEN)
tops.pack(side=TOP)
f1=Frame(root,width= 800, height= 700, relief= SUNKEN)
f1.pack(side=LEFT)
f2= Frame(root,width= 300, height= 700, bg= "powder blue", relief= SUNKEN)
f2.pack(side=RIGHT)
#****Local time ******
localtime= time.asctime(time.localtime(time.time()))

lb1info=Label(tops, font=("arial", 50, "bold"), text="Restaurant Management System", fg= "steel blue", bd= 10, anchor= "w")
lb1info.grid(row= 0 , column= 0)
lb1info=Label(tops, font=("arial", 19, "bold"), text=localtime, fg= "steel blue", bd= 10, anchor= "w")
lb1info.grid(row= 1 , column= 0)

#==========calculator=========

def btnclick(numbers):
    global operator
    operator = operator+str(numbers)
    text_input.set(operator)

def clearDisplay():
    global operator
    operator=""
    text_input.set("")
def btnequal2():
    global operator
    sumup= str(eval(operator))
    text_input.set(sumup)
    operator=""

def Ref():
    x= random.randint(10908, 500876)
    randomRef= str(x)
    rand.set(randomRef)


    CoFries = float(Fries.get())
    CoBurger= float(Burger.get())
    CoFillet= float(Fillet.get())
    CoChicken= float(Chicken.get())
    CoCheese= float(Cheese.get())
    CoDrinks= float(Drinks.get())


    CostofFries= CoFries*0.99
    CostofBurger= CoBurger* 1.00
    CostofFillet= CoFillet* 2.99
    CostofChicken= CoChicken*1.55
    CostofCheese= CoCheese* 0.55
    CostofDrinks= CoDrinks* 2.00


    CostofMeal= "$", str("%.2f" % (CostofFries+CostofBurger+CostofFillet+CostofChicken+CostofCheese+
                                   CostofDrinks))

    PayTax= ((CostofFries+CostofBurger+CostofFillet+CostofChicken+CostofCheese+
                                   CostofDrinks)* 0.2)

    TotalCost= (CostofFries+CostofBurger+CostofFillet+CostofChicken+CostofCheese+
                                   CostofDrinks)
    Ser_Charge= ((CostofFries+CostofBurger+CostofFillet+CostofChicken+CostofCheese+
                                   CostofDrinks)/99)

    Service= "$", str("%.2f" %Ser_Charge)

    OverAll= "$", str("%.2f" %(PayTax+TotalCost+Ser_Charge))
    PaidTax= "$", str("%.2f" %PayTax)

    service_charge.set(Service)
    Cost.set(CostofMeal)
    state_tax.set(PaidTax)
    sub_total.set(CostofMeal)
    Total.set(OverAll)




def qExit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Fillet.set("")
    Chicken.set("")
    Cheese.set("")
    Drinks.set("")
    Cost.set("")
    service_charge.set("")
    state_tax.set("")
    sub_total.set("")
    Total.set("")


txtDisplay= Entry(f2, font=("arial", 20, "bold"), textvariable= text_input, bd= 30, insertwidth= 4,
                  bg= "powder blue", justify= "right")
txtDisplay.grid(columnspan= 4)
btn7= Button(f2, padx=16, pady=16, bd= 8, fg="black", font= ("arial", 20, "bold"),
             text="7", bg= "powder blue", command= lambda: btnclick(7)).grid(row=2, column=0)
btn8= Button(f2, padx=16, pady=16, bd= 8, fg="black", font= ("arial", 20, "bold"),
             text="8", bg= "powder blue", command= lambda: btnclick(8)).grid(row=2, column=1)
btn9= Button(f2, padx=16, pady=16, bd= 8, fg="black", font= ("arial", 20, "bold"),
             text="9", bg= "powder blue", command= lambda: btnclick(9)).grid(row=2, column=2)
btnadd= Button(f2, padx=16, pady=16, bd= 8, fg="black", font= ("arial", 20, "bold"),
             text="+", bg= "powder blue", command= lambda: btnclick("+")).grid(row=2, column=3)
btn4= Button(f2, padx=16, pady=16, bd= 8, fg="black", font= ("arial", 20, "bold"),
             text="4", bg= "powder blue", command= lambda: btnclick(4)).grid(row=3, column=0)
btn5= Button(f2, padx=16, pady=16, bd= 8, fg="black", font= ("arial", 20, "bold"),
             text="5", bg= "powder blue", command= lambda: btnclick(5)).grid(row=3, column=1)
btn6= Button(f2, padx=16, pady=16, bd= 8, fg="black", font= ("arial", 20, "bold"),
             text="6", bg= "powder blue", command= lambda: btnclick(6)).grid(row=3, column=2)
btnsub= Button(f2, padx=16, pady=16, bd= 8, fg="black", font= ("arial", 20, "bold"),
             text="-", bg= "powder blue", command= lambda: btnclick("-")).grid(row=3, column=3)
btn1= Button(f2, padx=16, pady=16, bd= 8, fg="black", font= ("arial", 20, "bold"),
             text="1", bg= "powder blue", command= lambda: btnclick(1)).grid(row=4, column=0)
btn2= Button(f2, padx=16, pady=16, bd= 8, fg="black", font= ("arial", 20, "bold"),
             text="2", bg= "powder blue", command= lambda: btnclick(2)).grid(row=4, column=1)
btn3= Button(f2, padx=16, pady=16, bd= 8, fg="black", font= ("arial", 20, "bold"),
             text="3", bg= "powder blue", command= lambda: btnclick(3)).grid(row=4, column=2)
btnmul= Button(f2, padx=16, pady=16, bd= 8, fg="black", font= ("arial", 20, "bold"),
             text="*", bg= "powder blue", command= lambda: btnclick("*")).grid(row=4, column=3)
btn0= Button(f2, padx=16, pady=16, bd= 8, fg="black", font= ("arial", 20, "bold"),
             text="0", bg= "powder blue", command= lambda: btnclick(0)).grid(row=5, column=0)
btnC= Button(f2, padx=16, pady=16, bd= 8, fg="black", font= ("arial", 20, "bold"),
             text="C", bg= "powder blue", command= lambda: clearDisplay()).grid(row=5, column=1)
btnequal = Button(f2, padx=16, pady=16, bd= 8, fg="black", font= ("arial", 20, "bold"),
             text="=", bg= "powder blue", command= lambda: btnequal2()).grid(row=5, column=2)
btnDiv= Button(f2, padx=16, pady=16, bd= 8, fg="black", font= ("arial", 20, "bold"),
             text="/", bg= "powder blue", command= lambda: btnclick("/")).grid(row=5, column=3)

#==========the management system==================

rand= StringVar()
Fries= StringVar()
Burger= StringVar()
Fillet= StringVar()
Chicken= StringVar()
Cheese= StringVar()
Drinks= StringVar()
Cost= StringVar()
service_charge= StringVar()
state_tax= StringVar()
sub_total=StringVar()
Total= StringVar()

#----------restuarant info 1-------------
#=====Reference
lblreference= Label(f1, font=("arial", 16, "bold"), text= "Reference No.", bd=16, anchor= "w")
lblreference.grid(row=0, column=0)
txtreference= Entry(f1, font=("arial", 16, "bold"), textvariable= rand, bd=10, insertwidth=4,
                    bg= "powder blue", justify= "right")
txtreference.grid(row=0, column=1)


#=====Large Fries
lblFries= Label(f1, font=("arial", 16, "bold"), text= "Large Fries", bd=16, anchor= "w")
lblFries.grid(row=1, column=0)
txtFries= Entry(f1, font=("arial", 16, "bold"), textvariable= Fries, bd=10, insertwidth=4,
                    bg= "powder blue", justify= "right")
txtFries.grid(row=1, column=1)


#======Burger
lblBurger= Label(f1, font=("arial", 16, "bold"), text= "Burger Meal", bd=16, anchor= "w")
lblBurger.grid(row=2, column=0)
txtBurger= Entry(f1, font=("arial", 16, "bold"), textvariable= Burger, bd=10, insertwidth=4,
                    bg= "powder blue", justify= "right")
txtBurger.grid(row=2, column=1)

#=====Fillet
lblFillet= Label(f1, font=("arial", 16, "bold"), text= "Fillet O Meal", bd=16, anchor= "w")
lblFillet.grid(row=3, column=0)
txtFillet= Entry(f1, font=("arial", 16, "bold"), textvariable= Fillet, bd=10, insertwidth=4,
                    bg= "powder blue", justify= "right")
txtFillet.grid(row=3, column=1)
#=====Chicken


lblChicken= Label(f1, font=("arial", 16, "bold"), text= "Chicken Meal", bd=16, anchor= "w")
lblChicken.grid(row=4, column=0)
txtChicken= Entry(f1, font=("arial", 16, "bold"), textvariable= Chicken, bd=10, insertwidth=4,
                    bg= "powder blue", justify= "right")
txtChicken.grid(row=4, column=1)

#=====Cheese

lblCheese= Label(f1, font=("arial", 16, "bold"), text= "Burger Meal", bd=16, anchor= "w")
lblCheese.grid(row=5, column=0)
txtCheese= Entry(f1, font=("arial", 16, "bold"), textvariable= Cheese, bd=10, insertwidth=4,
                    bg= "powder blue", justify= "right")
txtCheese.grid(row=5, column=1)


#--------------Restuarant info 2---------------------------------


lblDrinks= Label(f1, font=("arial", 16, "bold"), text= "Drinks", bd=16, anchor= "w")
lblDrinks.grid(row=0, column=2)
txtDrinks= Entry(f1, font=("arial", 16, "bold"), textvariable= Drinks, bd=10, insertwidth=4,
                    bg= "powder blue", justify= "right")
txtDrinks.grid(row=0, column=3)


#=====Large Fries
lblCost= Label(f1, font=("arial", 16, "bold"), text= "Cost of Meal", bd=16, anchor= "w")
lblCost.grid(row=1, column=2)
txtCost= Entry(f1, font=("arial", 16, "bold"), textvariable= Cost, bd=10, insertwidth=4,
                    bg= "powder blue", justify= "right")
txtCost.grid(row=1, column=3)


#======Burger
lblService= Label(f1, font=("arial", 16, "bold"), text= "Service Charge", bd=16, anchor= "w")
lblService.grid(row=2, column=2)
txtService= Entry(f1, font=("arial", 16, "bold"), textvariable= service_charge, bd=10, insertwidth=4,
                    bg= "powder blue", justify= "right")
txtService.grid(row=2, column=3)

#=====Fillet
lblstateTax= Label(f1, font=("arial", 16, "bold"), text= "State Tax", bd=16, anchor= "w")
lblstateTax.grid(row=3, column=2)
txtstateTax= Entry(f1, font=("arial", 16, "bold"), textvariable= state_tax, bd=10, insertwidth=4,
                    bg= "powder blue", justify= "right")
txtstateTax.grid(row=3, column=3)
#=====Chicken


lblSubTotal= Label(f1, font=("arial", 16, "bold"), text= "Sub Total", bd=16, anchor= "w")
lblSubTotal.grid(row=4, column=2)
txtSubTotal= Entry(f1, font=("arial", 16, "bold"), textvariable= sub_total, bd=10, insertwidth=4,
                    bg= "powder blue", justify= "right")
txtSubTotal.grid(row=4, column=3)

#=====Cheese

lblTotalCost= Label(f1, font=("arial", 16, "bold"), text= "Total Cost", bd=16, anchor= "w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost= Entry(f1, font=("arial", 16, "bold"), textvariable= Total, bd=10, insertwidth=4,
                    bg= "powder blue", justify= "right")
txtTotalCost.grid(row=5, column=3)

#-------Buttons-------------

btntotal= Button(f1, padx= 16, pady=8, bd= 16, fg= "black", font=("arial", 16,"bold" ),
                 width= 10, text= "Total", bg= "powder blue", command= Ref).grid(row= 7, column= 1)

btnReset= Button(f1, padx= 16, pady=8, bd= 16, fg= "black", font=("arial", 16,"bold" ),
                 width= 10, text= "Reset", bg= "powder blue", command= reset).grid(row= 7, column= 2)

btnExit= Button(f1, padx= 16, pady=8, bd= 16, fg= "black", font=("arial", 16,"bold" ),
                 width= 10, text= "Exit", bg= "powder blue", command= qExit).grid(row= 7, column= 3)

root.mainloop()