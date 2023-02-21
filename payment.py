from tkinter import *
from main_interface import result, Id, Quantity, Days, selection_lblresult
import sqlite3
from tkinter import messagebox
from login_register import LoggedInGmail

def Database_connect():
    global conn, c
    conn = sqlite3.connect("Database.db")
    c = conn.cursor()



n=0
def Payment():
    result.config(text="")
    Id.config(state=NORMAL)
    Quantity.config(state=NORMAL)
    Days.config(state=NORMAL)
    Quantity.delete(0, END)
    Days.delete(0, END)
    Quantity.config(state=DISABLED)
    Days.config(state=DISABLED)  
    selection_lblresult.config(text="Lets Pay now")

    Database_connect()

    global n
    while n<1:
        try:
            c.execute("SELECT * FROM rent_record WHERE Email_Address=? and Amount=?", (LoggedInGmail, "Due"))
            desired_rows = c.fetchall()
            assert(desired_rows!=[]), "You have not any unpaid transaction"
            pass
        except AssertionError as msg:
            messagebox.showinfo('Halloween store', msg)
            break
        else:
            TotalUnpaidTransaction = len(desired_rows)
            messagebox.showinfo('Halloween store', "You have "+str(TotalUnpaidTransaction)+" unpaid transactions")
        
            response = messagebox.askyesno('Halloween store', "Pay now?")
            if response==YES:
                messagebox.showinfo('Halloween store', "Please enter which id you want to pay and proceed again")
                Id.config(state=NORMAL)
                n+=1
                break
            elif response==NO:
                result.config(text="Pay cancelled", fg="orange")
                break
    else:      
        try:
            id = Id.get()
            assert(id!="" and not id.isspace()), "Please complete the required field"
            pass
        except AssertionError as msg:
            result.config(text=msg, fg="red")
        else:
            try:
                c.execute("SELECT * FROM costume WHERE Costume_Id=?", (id,))
                assert(c.fetchone() is not None), "Invalid Id"
                pass
            except AssertionError as msg:
                result.config(text=msg, fg="red")
            else:
                try:
                    c.execute("SELECT * FROM  rent_record WHERE Email_Address=? and Amount=? and Costume_Id=?", (LoggedInGmail, "Due", id))
                    assert(c.fetchone() is not None), "you have not unpaid transaction for the given id"
                    
                    pass
                except AssertionError as msg:
                    result.config(text=msg, fg="red")
                else:
                    c.execute("UPDATE rent_record SET Amount=? Where Email_Address=? and Amount=? and Costume_Id=?", ("Paid", LoggedInGmail, "Due", id))
                    conn.commit()
                    response = messagebox.showinfo('Halloween store', " payment successful")
                
                    c.execute("SELECT * FROM rent_record WHERE Email_Address=? and Amount=?", (LoggedInGmail, "Due"))
                    if c.fetchall()!=[]:
                        response= messagebox.askyesno('Halloween store', 'Pay more?')
                        
                        if response==YES:
                            Id.delete(0, END)
                            result.config(text="Further payment processing...", fg="orange")

                        elif response==NO:
                            result.config(text="Further payment cancelled", fg="orange")
                            n=0
                    else:
                        messagebox.showinfo('Halloween store', "You have cleared all all your dues\nThankyou!")
                        
                        n=0
        