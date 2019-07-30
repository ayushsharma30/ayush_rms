from tkinter import *
import random
import time
root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management System")
root.configure(background="gray25")

text_Input = StringVar()
operator = ""

Tops = Frame(root, width = 1600,height = 50,bg="gray25", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800,height = 700,bg="gray25", relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300,height = 700, bg="gray25", relief=SUNKEN)
f2.pack(side=RIGHT)
#=========================Time================================
localtime=time.asctime(time.localtime(time.time()))
#===============================Info====================================
lblInfo = Label(Tops, font=('Times 50 bold'),text="Restaurant Management System",fg="brown3", bd=10,bg="gray25", anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops, font=('Times 25 bold'),text=localtime,fg="brown3", bd=10,bg="gray25", anchor='w')
lblInfo.grid(row=1,column=0)
#=======================Calculator=========================================
def btnClick(numbers):
    global operator
    operator= operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup =str(eval(operator))
    text_Input.set(sumup)
    operator=""

def Ref():
    x = random.randint(10908, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    CoFrench_Fries =float(French_Fries.get())
    CoBurger =float(Burger.get())
    CoVeg_Pizza =float(Veg_Pizza.get())
    CoCold_Drinks =float(Cold_Drinks.get())
    CoChinese_Platter =float(Chinese_Platter.get())
    CoVeg_Thaali =float(Veg_Thaali.get())

    CostofFrench_Fries = CoFrench_Fries * 40
    CostofBurger = CoBurger * 50
    CostofVeg_Pizza = CoVeg_Pizza * 90
    CostofCold_Drinks = CoCold_Drinks * 30
    CostofChinese_Platter = CoChinese_Platter * 150
    CostofVeg_Thaali = CoVeg_Thaali * 180

    CostofMeal = "Rs.", str('%.2f' % (CostofFrench_Fries + CostofBurger +  CostofVeg_Pizza
                                    + CostofCold_Drinks + CostofChinese_Platter
                                    + CostofVeg_Thaali))

    PayTax = ((CostofFrench_Fries + CostofBurger +  CostofVeg_Pizza
                                    + CostofCold_Drinks + CostofChinese_Platter
                                    + CostofVeg_Thaali) * 0.2)

    TotalCost = (CostofFrench_Fries + CostofBurger +  CostofVeg_Pizza
                                    + CostofCold_Drinks + CostofChinese_Platter
                                    + CostofVeg_Thaali)

    Ser_Charge = ((CostofFrench_Fries + CostofBurger +  CostofVeg_Pizza
                                    + CostofCold_Drinks + CostofChinese_Platter
                                    + CostofVeg_Thaali)/99)

    Service = "Rs.", str('%.2f' % Ser_Charge)
    OverAllCost = "Rs.", str('%.2f' % (PayTax + TotalCost + Ser_Charge))
    PaidTax = "Rs.", str('%.2f' % PayTax)
    Service_Charge.set(Service)
    Cost_Of_Meal.set(CostofMeal)
    GST.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total_Cost.set(OverAllCost)

def qExit():
    root.destroy()

def Reset():
    rand.set("")
    French_Fries.set("")
    Burger.set("")
    Veg_Pizza.set("")
    Cold_Drinks.set("")
    Chinese_Platter.set("")
    Veg_Thaali.set("")
    SubTotal.set("")
    Cost_Of_Meal.set("")
    Service_Charge.set("")
    GST.set("")
    Total_Cost.set("")
    
txtDisplay = Entry(f2,font=('Times 20 bold'),textvariable=text_Input, bd=30, insertwidth=4, bg="grey", justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8, fg="brown3", font=('Times 20 bold'),
            text="7", bg="grey", command=lambda: btnClick(7)).grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8, fg="brown3", font=('Times 20 bold'),
            text="8", bg="grey", command=lambda: btnClick(8)).grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8, fg="brown3", font=('Times 20 bold'),
            text="9", bg="grey", command=lambda: btnClick(9)).grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8, fg="brown3", font=('Times 20 bold'),
            text="+", bg="grey", command=lambda: btnClick("+")).grid(row=2,column=3)
#=================================Calculator Buttons Part-1===============================================================
btn4=Button(f2,padx=16,pady=16,bd=8, fg="brown3", font=('Times 20 bold'),
            text="4", bg="grey", command=lambda: btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8, fg="brown3", font=('Times 20 bold'),
            text="5", bg="grey", command=lambda: btnClick(5)).grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8, fg="brown3", font=('Times 20 bold'),
            text="6", bg="grey", command=lambda: btnClick(6)).grid(row=3,column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=8, fg="brown3", font=('Times 20 bold'),
            text="-", bg="grey", command=lambda: btnClick("-")).grid(row=3,column=3)
#=========================================Calculator Buttons Part-2========================================================
btn1=Button(f2,padx=16,pady=16,bd=8, fg="brown3", font=('Times 20 bold'),
            text="1", bg="grey", command=lambda: btnClick(1)).grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8, fg="brown3", font=('Times 20 bold'),
            text="2", bg="grey", command=lambda: btnClick(2)).grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=8, fg="brown3", font=('Times 20 bold'),
            text="3", bg="grey", command=lambda: btnClick(3)).grid(row=4,column=2)

Multiply=Button(f2,padx=16,pady=16,bd=8, fg="brown3", font=('Times 20 bold'),
            text="*", bg="grey", command=lambda: btnClick("*")).grid(row=4,column=3)
#=========================================Calculator Buttons Part-3=========================================================
btn0=Button(f2,padx=16,pady=16,bd=8, fg="brown3", font=('Times 20 bold'),
            text="0", bg="grey", command=lambda: btnClick(0)).grid(row=5,column=0)

btnClear=Button(f2,padx=16,pady=16,bd=8, fg="brown3", font=('Times 20 bold'),
            text="C", bg="grey", command=btnClearDisplay).grid(row=5,column=1)

btnEquals=Button(f2,padx=16,pady=16,bd=8, fg="brown3", font=('Times 20 bold'),
            text="=", bg="grey",command=btnEqualsInput).grid(row=5,column=2)

btn7=Button(f2,padx=16,pady=16,bd=8, fg="brown3", font=('Times 20 bold'),
            text="/", bg="grey",command=lambda: btnClick("/")).grid(row=5,column=3)
#============================Information 1======================================================================
rand = StringVar()
French_Fries = StringVar()
Burger = StringVar()
Veg_Pizza = StringVar()
Cold_Drinks = StringVar()
Chinese_Platter = StringVar()
Veg_Thaali = StringVar()
SubTotal = StringVar()
Cost_Of_Meal = StringVar()
Service_Charge = StringVar()
GST = StringVar()
Total_Cost = StringVar()

lblReference = Label(f1,font=('Times 18 bold'), text="Reference", fg="brown3", bd=16, bg="gray25", anchor='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('Times 18 bold'), textvariable=rand, bd=10, insertwidth=4,
                   bg="#ffffff", justify = 'right')
txtReference.grid(row=0,column=1)

lblFrench_Fries = Label(f1,font=('Times 18 bold'), text="French Fries(40)", fg="brown3", bd=16, bg="gray25", anchor='w')
lblFrench_Fries.grid(row=1,column=0)
txtFrench_Fries=Entry(f1,font=('Times 18 bold'), textvariable=French_Fries, bd=10, insertwidth=4,
                   bg="#ffffff", justify = 'right')
txtFrench_Fries.grid(row=1,column=1)

lblBurger = Label(f1,font=('Times 18 bold'), text="Burger(50)", fg="brown3", bd=16, bg="gray25", anchor='w')
lblBurger.grid(row=2,column=0)
txtBurger=Entry(f1,font=('Times 18 bold'), textvariable=Burger, bd=10, insertwidth=4,
                   bg="#ffffff", justify = 'right')
txtBurger.grid(row=2,column=1)

lblVeg_Pizza = Label(f1,font=('Times 18 bold'), text="Veg Pizza(90)", fg="brown3", bd=16, bg="gray25", anchor='w')
lblVeg_Pizza.grid(row=3,column=0)
txtVeg_Pizza=Entry(f1,font=('Times 18 bold'), textvariable=Veg_Pizza, bd=10, insertwidth=4,
                   bg="#ffffff", justify = 'right')
txtVeg_Pizza.grid(row=3,column=1)

lblChinese_Platter = Label(f1,font=('Times 18 bold'), text="Chinese Platter(150)", fg="brown3", bd=16, bg="gray25", anchor='w')
lblChinese_Platter.grid(row=4,column=0)
txtChinese_Platter=Entry(f1,font=('Times 18 bold'), textvariable=Chinese_Platter, bd=10, insertwidth=4,
                   bg="#ffffff", justify = 'right')
txtChinese_Platter.grid(row=4,column=1)

lblVeg_Thaali = Label(f1,font=('Times 18 bold'), text="Veg Thaali(180)", fg="brown3", bd=16, bg="gray25", anchor='w')
lblVeg_Thaali.grid(row=5,column=0)
txtVeg_Thaali=Entry(f1,font=('Times 18 bold'), textvariable=Veg_Thaali, bd=10, insertwidth=4,
                   bg="#ffffff", justify = 'right')
txtVeg_Thaali.grid(row=5,column=1)
#============================Information 2======================================================================
lblCold_Drinks = Label(f1,font=('Times 18 bold'), text="Cold Drinks(30)", fg="brown3", bd=16, bg="gray25", anchor='w')
lblCold_Drinks.grid(row=0,column=2)
txtCold_Drinks=Entry(f1,font=('Times 18 bold'), textvariable=Cold_Drinks, bd=10, insertwidth=4,
                   bg="#ffffff", justify = 'right')
txtCold_Drinks.grid(row=0,column=3)

lblCost_Of_Meal = Label(f1,font=('Times 18 bold'), text="Cost Of Meal", fg="brown3", bd=16, bg="gray25", anchor='w')
lblCost_Of_Meal.grid(row=1,column=2)
txtCost_Of_Meal=Entry(f1,font=('Times 18 bold'), textvariable=Cost_Of_Meal, bd=10, insertwidth=4,
                   bg="#ffffff", justify = 'right')
txtCost_Of_Meal.grid(row=1,column=3)

lblService_Charge = Label(f1,font=('Times 18 bold'), text="Service Charge", fg="brown3", bd=16, bg="gray25", anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge=Entry(f1,font=('Times 18 bold'), textvariable=Service_Charge, bd=10, insertwidth=4,
                   bg="#ffffff", justify = 'right')
txtService_Charge.grid(row=2,column=3)

lblGST = Label(f1,font=('Times 18 bold'), text="GST", fg="brown3", bd=16, bg="gray25", anchor='w')
lblGST.grid(row=3,column=2)
txtGST=Entry(f1,font=('Times 18 bold'), textvariable=GST, bd=10, insertwidth=4,
                   bg="#ffffff", justify = 'right')
txtGST.grid(row=3,column=3)

lblSubTotal = Label(f1,font=('Times 18 bold'), text="SubTotal", fg="brown3", bd=16, bg="gray25", anchor='w')
lblSubTotal.grid(row=4,column=2)
txtSubTotal=Entry(f1,font=('Times 18 bold'), textvariable=SubTotal, bd=10, insertwidth=4,
                   bg="#ffffff", justify = 'right')
txtSubTotal.grid(row=4,column=3)

lblTotal_Cost = Label(f1,font=('Times 18 bold'), text="Total Cost", fg="brown3", bd=16, bg="gray25", anchor='w')
lblTotal_Cost.grid(row=5,column=2)
txtTotal_Cost=Entry(f1,font=('Times 18 bold'), textvariable=Total_Cost, bd=10, insertwidth=4,
                   bg="#ffffff", justify = 'right')
txtTotal_Cost.grid(row=5,column=3)
#===========================Buttons At The Bottom in GUI=======================================================================
btnTotal=Button(f1,padx=16,pady=8, bd=16, fg="Black",font=('Times 18 bold'), width=10,
                text="Total", bg="Grey", command = Ref).grid(row=7, column=1)

btnReset=Button(f1,padx=16,pady=8, bd=16, fg="Black",font=('Times 18 bold'), width=10,
                text="Reset", bg="Grey", command = Reset).grid(row=7, column=2)

btnExit=Button(f1,padx=16,pady=8, bd=16, fg="Black",font=('Times 18 bold'), width=10,
                text="Exit", bg="Grey", command = qExit).grid(row=7, column=3)
root.mainloop()

