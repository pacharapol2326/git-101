from tkinter import*
from tkinter import ttk
import mysql.connector
import tkinter.messagebox
from openpyxl import Workbook

root =Tk()
root.geometry("1050x500+150+70")
root.title('บันทึกสินค้า')


db = mysql.connector.connect(
    host = 'localhost',
    port = 3306 ,
    user = 'root',
    password = 'password',
    database = 'store_1'
)
cursor = db.cursor()
# print(db) check con db



#label 
title = Label(text= "ชื่อสินค้า",pady=10).grid(row=0 )
price = Label(text='ราคา',pady=10).grid(row=1 )
total = Label(text='จำนวน (ชิ้น)',pady=10).grid(row=2 )
Label(text='ลบขอมูลด้วยเลข ID').place(x=20,y=400)




#entry
et1 = Entry(width=40)
et1.grid(row=0 ,column= 2 )

et2 = Entry(width=40)
et2.grid(row=1 ,column= 2 )

et3 = Entry(width=40)
et3.grid(row=2 ,column= 2)

et4 = Entry(width=40)
et4.place(x=120,y=400)






#Button insert

def add():
    title = et1.get()
    price = et2.get()
    total = et3.get()
  
    sql = '''
    INSERT INTO product (title,price,total)
    VALUES (%s,%s,%s);
      '''
    values = (title,price,total)
    cursor.execute(sql,values)    
    db.commit()

    if cursor.execute  :
        x = tkinter.messagebox.showinfo('บันทึก','บันทึกข้อมูลสำเร็จ')
        print(x,cursor.rowcount, "record inserted.")

    


       
        


#listbox for db---------------------------------------------------------------
def show ():
    cursor.execute("SELECT  id,title,price,total,created_at FROM product")
    record =cursor.fetchall()   
    for i ,(id,tital,price,total,created_at ) in enumerate(record , start=1):
        Listbox.insert("","end",values=(id,tital,price,total,created_at ))

  
        #  cursor.close()
        #  db.close
            
            
 
            
#delete 
def delete():    
    id = et4.get()
    sql = "Delete from product where id =%s"
    value = (id,)
    cursor.execute(sql,value)
    db.commit()

    if cursor.execute  :
        x = tkinter.messagebox.showinfo('Delete Data From sql','ลบข้อมูลสำเร็จ')
        print(x)
    
        

#-----------
    


colum1 = ('ID' , 'Tital' ,'Price' ,'Total' , 'Created_at')
Listbox = ttk.Treeview(root,columns=colum1, show='headings')

for col in colum1:
    Listbox.heading(col,text=col)
    Listbox.grid(row=1,column=0)
    Listbox.place(x=9,y=150)

#------------------------------------------------------------- Export Data


def export ():
    cursor = db.cursor()

    sql = '''
    SELECT*
    FROM product;
    '''
    cursor.execute(sql)
    product = cursor.fetchall()

    workbook = Workbook()
    sheet = workbook.active
    sheet.append(['ID','ชื่อสินค้า','ราคา','จำนวน (ชิ้น)','วันที่บันทึก'])

    for p in product:
        sheet.append(p)
        workbook.save(filename = 'ข้อมูลสินค้า.xlsx' )
    if cursor.execute  :
        tkinter.messagebox.showinfo('Export','Export data success')
        
        
 




def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)
    et3.delete(0,END)
    
#button



btn0 = Button(root,text="ล้างข้อมูล",fg='blue',bg= 'lightblue',command=deleteText).place(x=60,y=115)

btn1 = Button(root,text="บันทึกข้อมูล",fg='blue',bg= 'lightblue',command=add).place(x=140,y=115)

btn2 = Button(root,text="ดูข้อมูลทั้งหมด",fg='blue',bg= 'lightblue',command=show).place(x=240,y=115)

btn3 = Button(root,text="ลบข้อมูล",fg='blue',bg= 'lightblue',command=delete).place(x=380,y=400)

btn4 = Button(root,text="Export data to Excel",fg='blue',bg= 'lightblue',command=export).place(x=800,y=400)







root.mainloop()