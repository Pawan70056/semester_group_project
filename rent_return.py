from tkinter import *
import sqlite3
from tkinter import messagebox
from main_interface import RadioValues, Id, Quantity, Days, result, update_costumetable
from login_register import LoggedInGmail
import datetime

def database_connect():
    global conn, c
    conn = sqlite3.connect("Database.db")
    c=conn.cursor()


a=0
b=0
def MainEvent(which):
    if RadioValues.get()==1 and which=="Rent":
        try:
            id = Id.get()
            quantity = Quantity.get()
            days = Days.get()
            assert(id!="" and not id.isspace()) and (quantity!="" and not quantity.isspace()) and (days!="" and not days.isspace()), "Please complete all the fields"
            pass
        except AssertionError as msg:
            result.config(text=msg, fg="red") 
        else:
            try:
                database_connect()
                c.execute("SELECT * FROM costume WHERE Costume_Id=?",(id,))
                assert(c.fetchone() is not None), "Invalid Id"
                pass
            except AssertionError as msg:
                result.config(text=msg, fg="red")


            else:
                c.execute("SELECT * FROM costume WHERE Costume_Id=?", (id,))
                global InputId_rows
                InputId_rows = c.fetchone()
                try:
                    assert(quantity.isnumeric()), "Invalid quantity"
                    pass
                except AssertionError as msg:
                    result.config(text=msg, fg="red")
                else:
                    try:
                        assert(int(quantity)<=int(InputId_rows[4]) and int(quantity)>0), "Invalid quantity"
                        pass
                    except AssertionError as msg:
                        result.config(text=msg, fg="red")
                    else:
                        try:
                            assert(days.isnumeric()), "Invalid Day"
                            pass
                        except AssertionError as msg:
                            result.config(text=msg, fg="red")
                        else:
                            try:
                                assert(int(days)>0), "Invalid Day"
                                pass
                            except AssertionError as msg:
                                result.config(text=msg, fg="red")
                            else:                                                          
                                try:
                                    c.execute("SELECT * FROM rent_record WHERE Email_Address=? and Costume_Id=? and Status=?", (LoggedInGmail, id, "Has rented"))
                                    assert(c.fetchone() is None), "Sorry, you can't do transaction for the given id unless you return "
                                    pass
                                except AssertionError as msg:
                                    result.config(text=msg, fg="red")
                                else:
                                    try:
                                        c.execute("SELECT * FROM rent_record WHERE Email_Address=? and Costume_Id=? and Status=? and Amount=?", (LoggedInGmail, id, "Has returned", "Due"))
                                        assert(c.fetchone() is None), "Sorry, you can't do transaction for the given id unless you pay for it"
                                        pass
                                    except AssertionError as msg:
                                        result.config(text=msg, fg="red")
                                    else:
                                        global a 
                                        while a<1:        
                                            Response = messagebox.askokcancel('Halloween store', "Want to contine?\nIf you continue, there is no way to cancel rent")                             
                                            if Response==1:  
                                                response = messagebox.askyesno('Halloween store', "Do you want to rent more?")
                                                if response==YES or response==NO:
                                                    Id.delete(0, END)
                                                    Quantity.delete(0,END)
                                                    Days.delete(0,END)                                             
                                                    if response==YES:                                                
                                                        database_connect()
                                                        c.execute("UPDATE costume SET Quantity=:med1 WHERE Costume_Id=:id", {'med1':str(int(InputId_rows[4])-int(quantity)), 'id':id})
                                                        conn.commit()                                            
                                                        
                                                        c.execute("SELECT * FROM customer WHERE Email_Address=?", (LoggedInGmail,))
                                                        desired_rows = c.fetchone()
                                                        
                                                        first_name = desired_rows[1]
                                                        last_name = desired_rows[2]
                                                        global customer_name
                                                        customer_name = first_name + " " + last_name                                                    

                                                        c.execute("SELECT * FROM costume WHERE Costume_Id=?", (id,) )
                                                        desired_rows = c.fetchone()
                                                        costumename = str(desired_rows[1])
                                                        costumebrand = str(desired_rows[2])
                                                        price = str(desired_rows[3])       
                                                            
                                                        total_price01 = int(price) * int(quantity)

                                                        if int(days)>5:
                                                            extra_days = int(days)- 5
                                                            fine_per_day = 3
                                                            total_fine = extra_days * fine_per_day
                                                        else:
                                                            total_fine= 0
                                                            
                                                        total_price = total_price01 + total_fine
                                                            
                                                        now = datetime.datetime.now()
                                                        c.execute("INSERT into rent_record (Date , Time, Customer_Name, Costume_Id, Costume_Name, Brand, Price, Quantity, Days, Fine, Total_Price, Email_Address, Status, Amount) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"), customer_name, id, costumename, costumebrand, price, quantity, days, total_fine, total_price, LoggedInGmail, "Has rented", "Due"))
                                                        conn.commit()
                                                        conn.close()

                                                        messagebox.showinfo('Halloween store',"One rent success")
                                                        result.config(text="Rent processing...", fg="orange")

                                                        a+=1
                                                        break


                                                    elif response==NO :                                                                                        
                                                        c.execute("UPDATE costume SET Quantity=:med1 WHERE Costume_Id=:id", {'med1':str(int(InputId_rows[4])-int(quantity)), 'id':id})
                                                        conn.commit()
                                                        
                                                        update_costumetable()


                                                        c.execute("SELECT * FROM customer WHERE Email_Address=?", (LoggedInGmail,))
                                                        desired_rows = c.fetchone()                                   
                                                        first_name = desired_rows[1]
                                                        last_name = desired_rows[2]                                                 
                                                        customer_name = first_name + " " + last_name
                                                                

                                                        c.execute("SELECT * FROM costume WHERE Costume_Id=" + id )
                                                        desired_rows = c.fetchone()
                                                        costumename = str(desired_rows[1])
                                                        costumebrand = str(desired_rows[2])
                                                        price = str(desired_rows[3])
                                                                
                                                                
                                                        total_price01 = int(price) * int(quantity)

                                                        if int(days)>5:
                                                            extra_days = int(days)- 5
                                                            fine_per_day = 3
                                                            total_fine = extra_days * fine_per_day
                                                        else:
                                                            total_fine= 0
                                                                
                                                        total_price = total_price01 + total_fine
                                                        now = datetime.datetime.now()

                                                        c.execute("INSERT into rent_record (Date , Time, Customer_Name, Costume_Id, Costume_Name, Brand, Price, Quantity, Days, Fine, Total_Price, Email_Address, Status, Amount) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"), customer_name, id, costumename, costumebrand, price, quantity, days, total_fine, total_price, LoggedInGmail, "Has rented", "Due"))
                                                        conn.commit()
                                                        conn.close()

                                                        messagebox.showinfo('Halloween store',"Rented successfully\nThankyou!")
                                                        result.config(text="")
                                                        break
                                                        

                                            elif Response==0:
                                                result.config(text="Rent cancelled", fg="orange")
                                                break
                                                                                                                
                                            
                                        else:
                                            messagebox.showinfo('Halloween store',"Another rent success")
                                            database_connect()
                                            response = messagebox.askyesno('Halloween store', "Do you want to rent more?")
                                            if response==YES or response==NO:
                                                Id.delete(0, END)
                                                Quantity.delete(0,END)
                                                Days.delete(0,END)

                                                if response==YES:                                             
                                                    database_connect()

                                                    c.execute("UPDATE costume SET Quantity=:med1 WHERE Costume_Id=:id", {'med1':str(int(InputId_rows[4])-int(quantity)), 'id':id})
                                                    conn.commit()                                            
                                                        
                                                    c.execute("SELECT * FROM customer WHERE Email_Address=?", (LoggedInGmail,))
                                                    desired_rows = c.fetchone()                                                
                                                    first_name = desired_rows[1]
                                                    last_name = desired_rows[2]
                                                    customer_name = first_name + " " + last_name
                                                    
                                                    c.execute("SELECT * FROM costume WHERE Costume_Id=?", (id,) )
                                                    desired_rows = c.fetchone()
                                                    costumename = str(desired_rows[1])
                                                    costumebrand= str(desired_rows[2])
                                                    price = str(desired_rows[3])
                                                                
                                                            
                                                    total_price01 = int(price) * int(quantity)

                                                    if int(days)>5:
                                                        extra_days = int(days)- 5
                                                        fine_per_day = 3
                                                        total_fine = extra_days * fine_per_day
                                                    else:
                                                        total_fine= 0
                                                            
                                                    total_price = total_price01 + total_fine
                                                            
                                                    now = datetime.datetime.now()
                                                    c.execute("INSERT into rent_record (Date , Time, Customer_Name, Costume_Id, Costume_Name, Brand, Price, Quantity, Days, Fine, Total_Price, Email_Address, Status, Amount) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"), customer_name, id, costumename, costumebrand, price, quantity, days, total_fine, total_price, LoggedInGmail, "Has rented","Due"))
                                                    conn.commit()
                                                    conn.close()

                                                    

                                                    result.config(text="Rent processing", fg="orange")


                                                elif response==NO :                         
                                                        
                                                        c.execute("UPDATE costume SET Quantity=:med1 WHERE Costume_Id=:id", {'med1':str(int(InputId_rows[4])-int(quantity)), 'id':id})
                                                        conn.commit()
                                                    

                                                        update_costumetable()


                                                        c.execute("SELECT * FROM customer WHERE Email_Address=?", (LoggedInGmail,))
                                                        desired_rows = c.fetchone()                                                           
                                                        first_name = desired_rows[1]
                                                        last_name = desired_rows[2]                                                   
                                                        customer_name = first_name + " " + last_name
                                                                

                                                        c.execute("SELECT * FROM costume WHERE Costume_Id=?", (id,) )
                                                        desired_rows = c.fetchone()
                                                        costumename = str(desired_rows[1])
                                                        costumebrand = str(desired_rows[2])
                                                        price = str(desired_rows[3])
                                                                
                                                                
                                                        total_price01 = int(price) * int(quantity)

                                                        if int(days)>5:
                                                            extra_days = int(days)- 5
                                                            fine_per_day = 3
                                                            total_fine = extra_days * fine_per_day
                                                        else:
                                                            total_fine= 0
                                                                
                                                        total_price = total_price01 + total_fine
                                                        now = datetime.datetime.now()


                                                        c.execute("INSERT into rent_record (Date , Time, Customer_Name, Costume_Id, Costume_Name, Brand, Price, Quantity, Days, Fine, Total_Price, Email_Address, Status, Amount) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"), customer_name, id, costumename, costumebrand, price, quantity, days, total_fine, total_price, LoggedInGmail, "Has rented","Due"))
                                                        conn.commit()
                                                        conn.close()


                                                        messagebox.showinfo('Halloween store',"Rented successfully\nThankyou!")
                                                        result.config(text="")
                                                        a=0
                                                                        

    elif RadioValues.get()==2 and which=="Return":
        try:
            id = Id.get()
            assert(id!="" and not id.isspace()), "Please complete the required field"
            pass
        except AssertionError as msg:
            result.config(text=msg, fg="red")
        else:
            try:
                database_connect()
                c.execute("SELECT * FROM  costume WHERE Costume_Id=?", (id,))             
                assert(c.fetchone() is not None), "Invalid Id"
                pass
            except AssertionError as msg:
                result.config(text=msg, fg="red")
            else:
                try:
                    c.execute("SELECT * FROM rent_record WHERE EMAIL_ADDRESS=? and Costume_Id=? and Status=?", (LoggedInGmail, id, "Has rented"))
                    desired_rows = c.fetchone()    
                    assert(desired_rows is not None), "You have not rented the given id costume"
                    pass
                except AssertionError as msg:
                    result.config(text=msg, fg="orange")
                else:
                    Quantity.config(state=NORMAL)
                    Days.config(state=NORMAL)
                    rented_quantity = desired_rows[7]
                    rented_days = desired_rows[8]
                    Quantity.delete(0, END)
                    Days.delete(0,END)
                    Quantity.insert(0, rented_quantity)
                    Days.insert(0, rented_days)
                    Quantity.config(state=DISABLED)
                    Days.config(state=DISABLED)

                    global b
                    while b<1:
                        response = messagebox.askokcancel('Halloween store', 'Want to continue? If you continue, there is no way to cancel return')
                        if response==1:
                            response = messagebox.askyesno('Halloween store', 'Do you want to return more?')
                            if response==YES or response==NO:
                                Id.delete(0, END)
                                Quantity.config(state=NORMAL)
                                Days.config(state=NORMAL)
                                Quantity.delete(0, END)
                                Days.delete(0,END)
                                Quantity.config(state=DISABLED)
                                Days.config(state=DISABLED)

                                if response==YES:
                                    c.execute("UPDATE rent_record SET Status=? WHERE Email_Address=? and Costume_Id=?", ("Has returned", LoggedInGmail, id))
                                    conn.commit()

                                    c.execute("SELECT * FROM costume WHERE Costume_Id=?", id)
                                    desired_rows = c.fetchone()
                                    remained_quantity = desired_rows[4]

                                    c.execute("UPDATE costume SET Quantity=? WHERE Costume_Id=?", (str(int(remained_quantity) + int(rented_quantity)), id))
                                    conn.commit()
                                    conn.close()

                                    messagebox.showinfo('Halloween store', "One return success")
                                    result.config(text="Return processing", fg="orange")
                                    b+=1
                                    break
                                                            

                                elif response==NO:                             
                                    c.execute("UPDATE rent_record SET Status=? WHERE Email_Address=? and Costume_Id=?", ("Has returned", LoggedInGmail, id))
                                    conn.commit()

                                    c.execute("SELECT * FROM costume WHERE Costume_Id=?", (id,))
                                    desired_rows = c.fetchone()
                                    remained_quantity = desired_rows[4]

                                    c.execute("UPDATE costume SET Quantity=? WHERE Costume_Id=?", (str(int(remained_quantity) + int(rented_quantity)), id))
                                    conn.commit()

                                    update_costumetable()

                                    conn.close()

                                    messagebox.showinfo('Halloween store', "Returned successfully\nThankyou!")
                                    result.config(text="")
                                    break
                                                                
                                                        
                        elif response==0:
                            result.config(text="Return cancelled", fg="orange")
                            break

                    else:
                        messagebox.showinfo('Halloween store',"Another return success")
                        response = messagebox.askyesno('Halloween store', 'Do you want to return more?')
                        if response==YES or response==NO:
                            Id.delete(0, END)
                            Quantity.config(state=NORMAL)
                            Days.config(state=NORMAL)
                            Quantity.delete(0, END)
                            Days.delete(0,END)
                            Quantity.config(state=DISABLED)
                            Days.config(state=DISABLED)

                            if response==YES:
                                c.execute("UPDATE rent_record SET Status=? WHERE Email_Address=? and Costume_Id=?", ("Has returned", LoggedInGmail, id))
                                conn.commit()

                                c.execute("SELECT * FROM costume WHERE Costume_Id=?", id)
                                desired_rows = c.fetchone()
                                remained_quantity = desired_rows[4]

                                c.execute("UPDATE costume SET Quantity=? WHERE Costume_Id=?", (str(int(remained_quantity) + int(rented_quantity)), id))
                                conn.commit()
                                conn.close()
                                result.config(text="Return processing", fg="orange")
                                                            

                            elif response==NO:                             
                                c.execute("UPDATE rent_record SET Status=? WHERE Email_Address=? and Costume_Id=?", ("Has returned", LoggedInGmail, id))
                                conn.commit()

                                c.execute("SELECT * FROM costume WHERE Costume_Id=?", id)
                                desired_rows = c.fetchone()
                                remained_quantity = desired_rows[4]

                                c.execute("UPDATE costume SET Quantity=? WHERE Costume_Id=?", (str(int(remained_quantity) + int(rented_quantity)), id))
                                conn.commit()

                                update_costumetable()

                                conn.close()

                                messagebox.showinfo('Halloween store', "Returned successfully\nThankyou!")
                                result.config(text="")
                                
                                b=0

    else:
        pass