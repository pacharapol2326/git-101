from tkinter import *
from tkinter import ttk 


root =Tk()
root.title("แปลงสกุลเงิน")
root.geometry("450x130+300+70") 


# Input
money = IntVar()
Label(text='จำนวนเงิน (THB)',padx=10,font=30,background='red').grid(row=0, sticky=W)
et1 = Entry(font=30,width=30,textvariable=money,bg='blue')   #width 8วามกว้างในช่องกรอกข้อความ 
et1.grid(row=0,column=1)


choice = StringVar(value= "โปรดเลือกสกุลเงิน")
Label(text='เลือกสกุลเงิน',padx=10,font=30).grid(row=1,sticky=W)
combo =ttk.Combobox(width=20,font=30,textvariable=choice)
combo['values']=('EUR',"JPY",'USD','GBP')
combo.grid(row=1,column=1)




#output
Label(text='ผลการคำนวน',padx=10,font=30).grid(row=2, sticky=W)
et2 = Entry(font=30,width=30)   #width 8วามกว้างในช่องกรอกข้อความ 
et2.grid(row=2,column=1)

def calculate():
     amount = money.get()
     currency =choice.get()

     if currency == "EUR":
          et2.delete(0,END)
          result = ((amount *0.027),"EUR(ยูโร)")
          et2.insert(0,result)

     elif currency == "JPY":
         et2.delete(0,END)
         result = ((amount *3.90),"JPY(เยน)")
         et2.insert(0,result)
        
     elif currency == "USD":
        et2.delete(0,END)
        result = ((amount *0.029),"USD($)")
        et2.insert(0,result)
          
     elif currency == "GBP":
        et2.delete(0,END)
        result = ((amount *0.024),"GBP(ปอน)")
        et2.insert(0,result)
          
     else :
        et2.delete(0,END)
        result = "ไม่พบข้อมูล"
        et2.insert(0,result)

          
def deleteText ():
    et1.delete(0,END)
    et2.delete(0,END)


Button(text="คำนวณ",font=30,width=10,command=calculate).grid(row=3,column=1,sticky=W)
Button(text="ล้าง",font=30,width=10,command=deleteText).grid(row=3,column=1,sticky=E)




























root.mainloop()

