from tkinter import *
from tkinter import messagebox
import sqlite3
from main_interface import selection_lblresult, Id, Quantity, Days, result, root, filemenu01
from login_register import LoggedInGmail
import datetime


def Database_connect():
    global conn, c
    conn = sqlite3.connect("Database.db")
    c = conn.cursor()

def invoice_processing(which):
    
    selection_lblresult.config(text="")
    Id.config(state=NORMAL)
    Quantity.config(state=NORMAL)
    Days.config(state=NORMAL)
    Id.delete(0, END)
    Quantity.delete(0, END)
    Days.delete(0, END)
    Id.config(state=DISABLED)
    Quantity.config(state=DISABLED)
    Days.config(state=DISABLED)
    result.config(text="")
    
    if which=="Rent invoice":
        try:
            Database_connect()
            c.execute("SELECT * From rent_record WHERE Email_Address=? and Status=?", (LoggedInGmail, "Has rented"))
            assert(c.fetchone() is not None), "Sorry, you have not any recent rent transaction"
            pass
        except AssertionError as msg:
            result.config(text=msg,fg="orange")
        else:
            result.config(text="...generating invoice", fg="orange")
            root.after(3000, lambda:result.config(text="Please download rent invoice from file menu"))
            filemenu01.entryconfig("Save as txt", command=rent_invoice, state=NORMAL)
            
    
    elif which=="Return invoice":
        try:
            Database_connect()
            c.execute("SELECT * FROM rent_record WHERE Email_Address=? and Status=?", (LoggedInGmail, "Has returned"))
            assert(c.fetchone() is not None), "Sorry, you have not any recent return transaction"
            pass
        except AssertionError as msg:
                result.config(text=msg, fg="orange")
        else:
            result.config(text="generating invoice...", fg="orange")
            root.after(3000, lambda:result.config(text="Please download return invoice from file"))
            filemenu01.entryconfig("Save as txt", command=return_invoice, state=NORMAL)

       







def rent_invoice():
        c.execute("SELECT * FROM customer WHERE Email_Address=?", (LoggedInGmail,))
        desired_row = c.fetchone()
        first_name = desired_row[1]
        last_name = desired_row[2]
        cus_name = first_name + " " + last_name


        c.execute("SELECT * FROM rent_record WHERE Email_Address=? and Status=? and Amount=?", (LoggedInGmail, "Has rented", "Due"))
        desired_rows = c.fetchall()
        total_dues = 0
        if desired_rows!=[]:
            for record in desired_rows:
                total_dues+= int(record[10])
        

        c.execute("SELECT * FROM rent_record WHERE Email_Address=? and Status=? and Amount=?", (LoggedInGmail, "Has rented", "Paid"))
        desired_rows = c.fetchall()
        total_paid = 0
        if desired_rows!=[]:
            for record in desired_rows:
                total_paid += int(record[10])

        

        c.execute("SELECT * From rent_record WHERE Email_Address=? and Status=?", (LoggedInGmail, "Has rented"))
        desired_rows = c.fetchall()
        print_records = ""
        grand_total = 0
        for record in desired_rows:
            print_records += str(record[3]) + "\t\t   " + str(record[4]) + "\t\t" + str(record[5]) + "\t\t\t" + str(record[6]) + "\t\t\t   " + str(record[7]) + "\t\t" + str(record[8]) + "\t\t " + str(record[9]) + "\t\t\t   " + str(record[10]) + "\t\t\t  " +str(record[13]) + "\n"
            grand_total += int(record[10])
        


        now = datetime.datetime.now()
        filename = first_name + "_" + last_name + str(now.strftime("%Y%m%d_%H%M%S"))    
        file = open(filename, 'w')
        file.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++Rent Invoice+++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        file.write("\t\t\t\t\t\t\t\t\t\t\t\t  Halloween Costumes\n")
        file.write("Date:"+str(now.strftime("%Y-%m-%d"))+"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t" +"Time"+":"+str(now.strftime("%H:%M:%S")+"\n"))
        file.write("Name:"+cus_name+"\n")
        file.write("----------------------------------------------------------------------------------------------------------------------\n")
        file.write("Id no.\t\tCostume name \t\t Brand \t\t Price($)\t\tQuantity\tDays\tFine($)\t  Total_Price($)\tRemarks\n")
        file.write("----------------------------------------------------------------------------------------------------------------------\n")
        file.write(print_records)
        file.write("----------------------------------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   Grand Total:"+str(grand_total)+"$"+"\n")
        file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTotal Dues:"+str(total_dues)+"$"+"\n")
        file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTotal Paid:"+str(total_paid)+"$"+"\n")
        file.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        file.write(" \t\t\t\t\t\t\t\t\t\t\t Thank you for visiting us\n\t\t\t\t\t\t\t\t\t\t\t   Have a nice day ahead\n")
        file.write("Proprietors:Ayush Ghimire\n\t\t\tBasanta Khand\n\t\t\tPawan Chaudhary\nContact us :9750000000\n")
        file.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        file.close()

        
        messagebox.showinfo('Halloween store', "Rent receipt downloaded")
        result.config(text="")
        filemenu01.entryconfig("Save as txt", state=DISABLED)

       




def return_invoice():
        c.execute("SELECT * FROM customer WHERE Email_Address=?", (LoggedInGmail,))
        desired_row = c.fetchone()
        first_name = desired_row[1]
        last_name = desired_row[2]
        cus_name = first_name + " " + last_name


        c.execute("SELECT * FROM rent_record WHERE Email_Address=? and Status=? and Amount=?", (LoggedInGmail, "Has returned", "Due"))
        desired_rows = c.fetchall()
        total_dues = 0
        if desired_rows !=[]:
            for record in desired_rows:
                total_dues +=int(record[10])
        
        

        c.execute("SELECT * FROM rent_record WHERE Email_Address=? and Status=? and Amount=?", (LoggedInGmail, "Has returned", "Paid"))
        desired_rows = c.fetchall()
        total_paid = 0
        if desired_rows!=[]:
            for record in desired_rows:
                total_paid +=int(record[10])
        
       
        

        
        c.execute("SELECT * From rent_record WHERE Email_Address=? and Status=?", (LoggedInGmail, "Has returned"))
        desired_rows = c.fetchall()
        print_records = ""
        grand_total = 0
        for record in desired_rows:
            print_records += str(record[3]) + "\t\t   " + str(record[4]) + "\t\t" + str(record[5]) + "\t\t\t" + str(record[6]) + "\t\t\t   " + str(record[7]) + "\t\t" + str(record[8]) + "\t\t " + str(record[9]) + "\t\t\t   " + str(record[10]) + "\t\t\t  " + str(record[13]) + "\n"
            grand_total += int(record[10])
        
    

        now = datetime.datetime.now()
        filename = first_name + "_" + last_name + str(now.strftime("%Y%m%d_%H%M%S"))    
        file = open(filename, 'w')
        file.write("++++++++++++++++++++++++++++++++++++++++++++++++++++Return Invoice++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        file.write("\t\t\t\t\t\t\t\t\t\t\t\t  Halloween Costumes\n")
        file.write("Date:"+str(now.strftime("%Y-%m-%d"))+"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t" +"Time"+":"+str(now.strftime("%H:%M:%S")+"\n"))
        file.write("Name:"+cus_name+"\n")
        file.write("----------------------------------------------------------------------------------------------------------------------\n")
        file.write("Id no.\t\tCostume name \t\t Brand \t\t Price($)\t\tQuantity\tDays\tFine($)\t  Total_Price($)\tRemarks\n")
        file.write("----------------------------------------------------------------------------------------------------------------------\n")
        file.write(print_records)
        file.write("----------------------------------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   Grand Total:"+str(grand_total)+"$"+"\n")
        file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTotal Dues:"+str(total_dues)+"$"+"\n")
        file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTotal Paid:"+str(total_paid)+"$"+"\n")
        file.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        file.write(" \t\t\t\t\t\t\t\t\t\t\t Thank you for visiting us\n\t\t\t\t\t\t\t\t\t\t\t   Have a nice day ahead\n")
        file.write("Proprietors:Ayush Ghimire\n\t\t\tBasanta Khand\n\t\t\tPawan Chaudhary\nContact us :9750000000\n")
        file.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        file.close()

        
        messagebox.showinfo('Halloween store', "Return receipt downloaded")
        filemenu01.entryconfig("Save as txt", state=DISABLED)