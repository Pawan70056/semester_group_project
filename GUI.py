from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk
import datetime
from tkinter import ttk



root = Tk()
root.title("Halloween Store")
root_icon = PhotoImage(file="./icon/pumpkin.png")
root.iconphoto("Feary Pumpkin", root_icon)





width = 1250
height = 760
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))




imageframe = Frame(root)
imageframe.pack()
my_image = Image.open('./icon/dream_bat.png')
resized_image = my_image.resize((700,200))
converted_image = ImageTk.PhotoImage(resized_image)
image_lbl = Label(imageframe, image = converted_image)
image_lbl.pack( )



    
def Database_connect():
    global conn, c
    conn = sqlite3.connect("Database.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS `customer` (Email_Address TEXT, First_Name TEXT, Last_Name TEXT, Contact_Number TEXT, Date_Of_Birth TEXT, Username TEXT, Password TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS `rent_record` (Date TEXT, Time TEXT, Customer_Name TEXT, Costume_Id TEXT, Costume_Name TEXT, Brand TEXT, Price TEXT, Quantity TEXT, Days TEXT, Fine TEXT, Total_Price TEXT, Email_Address TEXT, Status TEXT, Amount TEXT)")




EMAILADDRESS = StringVar()
FIRSTNAME = StringVar()
LASTNAME = StringVar()
DATEOFBIRTH = StringVar()
USERNAME = StringVar()
PASSWORD = StringVar()
CONTACT = StringVar()




def LoginForm():
    global headframe1, lbl_result1
    headframe1= Frame(root)
    headframe1.pack(pady=10)
    LabelFrame1 = Frame(headframe1)
    LabelFrame1.pack(pady=10)
    label01 = Label(LabelFrame1, text="Please log in to your account here !!", font=('calibri & Bold', 25))
    label01.pack()


    LoginFrame = Frame(headframe1)
    LoginFrame.pack(pady=10)
    lbl_emailaddress = Label(LoginFrame, text="Email address", font= ('calibri', 20))
    lbl_emailaddress.grid(row=1)
    lbl_password = Label(LoginFrame, text="Password", font=('calibri', 20))
    lbl_password.grid(row=2)
    lbl_result1 = Label(LoginFrame, text="", font=('calibri', 20))
    lbl_result1.grid(row=3, columnspan=2)
    emailaddress = Entry(LoginFrame, font=('calibri', 15), textvariable=EMAILADDRESS)
    emailaddress.grid(row=1, column=1)
    password = Entry(LoginFrame, font=('calibri', 15), textvariable=PASSWORD, show="*")
    password.grid(row=2, column=1)
    login_btn = Button(LoginFrame, text="Login", font=('calibri', 20), width =35, bg="green", command=Login)
    login_btn.grid(row=4, columnspan=2)


    LabelFrame2 = Frame(headframe1)
    LabelFrame2.pack(side=LEFT)  
    label02 = Label(LabelFrame2, text="Don't have any accounts?", font=('calibri', 20))
    label02.grid(row=0)
    lbl_register = Label(LabelFrame2, text="Register now", font=('calibri', 15), fg="blue")
    lbl_register.grid(row=0, column=1)
    lbl_register.bind('<Button-1>', ToggleToRegister)
     
    


def RegisterForm():
    global headframe2, lbl_result2
    headframe2= Frame(root)
    headframe2.pack(pady=10)
    LabelFrame1 = Frame(headframe2)
    LabelFrame1.pack(pady=10)
    label01 = Label(LabelFrame1, text="\t\tRegister into Halloween Store and explore your desires !!", font=('calibri & Bold', 25))
    label01.pack()


    RegisterFrame = Frame(headframe2)
    RegisterFrame.pack()
    lbl_emailaddress = Label(RegisterFrame, text="       Email address", font=('calibri',20))
    lbl_emailaddress.grid(row=0)
    lbl_firstname = Label(RegisterFrame, text=" First name", font=('calibri', 20))
    lbl_firstname.grid(row=1)
    lbl_lastname = Label(RegisterFrame, text=" Last name", font=('calibri', 20))
    lbl_lastname.grid(row=2)  
    lbl_dateofbirth = Label(RegisterFrame, text="     Date of birth", font=('calibri', 20))
    lbl_dateofbirth.grid(row=3)
    lbl_username = Label(RegisterFrame, text=" Username", font=('calibri', 20))
    lbl_username.grid(row=4)
    lbl_password = Label(RegisterFrame, text="Password", font=('calibri', 20))
    lbl_password.grid(row=5)
    lbl_phonenumber = Label(RegisterFrame, text="   Contact no.", font=('calibri',20))
    lbl_phonenumber.grid(row=6)
    lbl_result2 = Label(RegisterFrame, text="", font=('calibri', 20))
    lbl_result2.grid(row=7, columnspan=2)
    emailaddress = Entry(RegisterFrame, font=('calibri', 15), textvariable=EMAILADDRESS)
    emailaddress.grid(row=0, column=1)
    firstname = Entry(RegisterFrame, font=('calibri', 15), textvariable=FIRSTNAME)
    firstname.grid(row=1, column=1)
    lastname = Entry(RegisterFrame, font=('calibri', 15), textvariable=LASTNAME)
    lastname.grid(row=2, column=1)
    dateofbirth = Entry(RegisterFrame, font=('calibri', 15), textvariable=DATEOFBIRTH)
    dateofbirth.grid(row=3, column=1)
    username = Entry(RegisterFrame, font=('calibri', 15), textvariable=USERNAME)
    username.grid(row=4, column=1)
    password = Entry(RegisterFrame, font=('calibri', 15), textvariable=PASSWORD, show="*")
    password.grid(row=5, column=1)
    phonenumber= Entry(RegisterFrame, font=('calibri', 15), textvariable=CONTACT)
    phonenumber.grid(row=6, column=1)
    login_btn = Button(RegisterFrame, text="Register", font=('calibri', 20), width=35, bg="green", command=Register)
    login_btn.grid(row=8, columnspan=2)


    LabelFrame2 = Frame(headframe2)
    LabelFrame2.pack(pady=10)
    label02 = Label(LabelFrame2, text="Already have an account?", font=('calibri',20))
    label02.grid(row=0, column=0)
    lbl_login = Label(LabelFrame2, text="Login", fg="Blue", font=('calibri', 15))
    lbl_login.grid(row=0, column=1)   
    lbl_login.bind('<Button-1>', ToggleToLogin)




def ToggleToLogin(event=None):
    headframe2.destroy()
    LoginForm()
 



def ToggleToRegister(event=None):
    headframe1.destroy()
    RegisterForm()




def Register():
    Database_connect()

    emailaddress = EMAILADDRESS.get()
    firstname = FIRSTNAME.get()
    lastname = LASTNAME.get()
    dateofbirth = DATEOFBIRTH.get()
    username = USERNAME.get()
    password = PASSWORD.get()
    contact = CONTACT.get()

    if (EMAILADDRESS.get()=="" or emailaddress.isspace()) or (FIRSTNAME.get()=="" or firstname.isspace()) or (LASTNAME.get()=="" or lastname.isspace()) or (DATEOFBIRTH.get()=="" or dateofbirth.isspace()) or (USERNAME.get()=="" or username.isspace()) or (PASSWORD.get()=="" or password.isspace()) or (CONTACT.get()=="" or contact.isspace()):
        lbl_result2.config(text="Please complete all the fields", fg="red", font=('calibri', 15) )
    else:
        c.execute("SELECT * FROM `customer` WHERE `Email_Address`=? or `Username`=?", (EMAILADDRESS.get(), USERNAME.get()))
        data = c.fetchone()
        if data is not None:
            fetch = 0
            while fetch<len(data):
                if data[fetch]==EMAILADDRESS.get():
                    lbl_result2.config(text="This email address already have an account!", font=('calibri', 15), fg="orange")
                    break
                fetch+=1
            else:
                lbl_result2.config(text="Username is already taken", font=('calibri', 15), fg="orange")
 
        else:
            c.execute("INSERT INTO `customer` (Email_Address, First_Name, Last_Name, Contact_Number, Date_Of_Birth, Username, Password) VALUES(?, ?, ?, ?, ?, ?, ?)", (str(EMAILADDRESS.get()), str(FIRSTNAME.get()), str(LASTNAME.get()), str(CONTACT.get()), str(DATEOFBIRTH.get()), str(USERNAME.get()), str(PASSWORD.get())))
            conn.commit()
            FIRSTNAME.set("")
            LASTNAME.set("")
            CONTACT.set("")
            EMAILADDRESS.set("")
            DATEOFBIRTH.set("")
            USERNAME.set("")
            PASSWORD.set("") 
            lbl_result2.config(text="Successfully Created", fg="green", font=('calibri', 15))


        c.close()
        conn.close()




def Login():
    Database_connect()
    email_address = EMAILADDRESS.get()
    password = PASSWORD.get()

    if (EMAILADDRESS.get()=="" or email_address.isspace()) or (PASSWORD.get()=="" or password.isspace()):
        lbl_result1.config(text="Please complete all the fields", font=('calibri', 15), fg="red")  
    else:
        c.execute("SELECT * FROM `customer` WHERE `Email_Address`=? and `Password`=?", (EMAILADDRESS.get(), PASSWORD.get()))
        if c.fetchone() is not None:
            # lbl_result1.config(text="Successfully Logged In", fg="green", font=('calibri', 15))
            login_success()
        else:
            lbl_result1.config(text="Invalid user-email or password", fg="red", font=('calibri', 15))
    



LoginForm()




def login_success():
    imageframe.destroy()
    headframe1.destroy()
    global LoggedInGmail
    LoggedInGmail = EMAILADDRESS.get()
    success_frame = Frame(root)
    success_label = Label(success_frame, text="You successfully logged in as "+str(LoggedInGmail)+".", font=('calibri',11), fg="green")
    success_label.pack()
    root.after(2000, success_frame.pack())
    root.after(3000, success_label.destroy)
    main_interface()



def selection():
    value = RadioValues.get()
    if value==1 or value==2:
        if value==1 or value ==2:
            King_frame.destroy()
            main_interface()
                    
            Id.config(state=NORMAL)
            Quantity.config(state=NORMAL)
            Days.config(state=NORMAL)
                    
            Id.delete(0, END)
            Quantity.delete(0, END)
            Days.delete(0, END)
            

            if value==1:
                RadioValues.set(1)
                selection_lblresult.config(text="Let's rent costume", font=('calibri', 18), fg="green")
            
      
            elif value==2:
                RadioValues.set(2)
                Quantity.config(state=DISABLED)
                Days.config(state=DISABLED)
                selection_lblresult.config(text="Let's return costume", font=('calibri',18), fg="green")

    else:
        King_frame.destroy()
        main_interface()
        RadioValues.set(3)
        selection_lblresult.config(text="Let's see some of our sample costumes", font=('calibri',18), fg="green")
        
        Gallery()



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
                Database_connect()
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
                                                        Database_connect()
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
                                            Database_connect()
                                            response = messagebox.askyesno('Halloween store', "Do you want to rent more?")
                                            if response==YES or response==NO:
                                                Id.delete(0, END)
                                                Quantity.delete(0,END)
                                                Days.delete(0,END)

                                                if response==YES:                                             
                                                    Database_connect()

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
                Database_connect()
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
    global filemenu01
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
        
            
                    






def Gallery():
    recordframe01.destroy()
    recordframe02.destroy()
    recordframe03.destroy()
    recordframe04.destroy()
    recordframe05.destroy()
    TableFrame.config(text="", bg="red")
    dash_frame.destroy()
    EntryFrame.destroy()
    resultframe.destroy()
    ButtonFrame.destroy()


  
    image_dict = {
        "Pirate costume sample": "./halloween_images/pirate.png",
        "Corset costume sample": "./halloween_images/corset.png",
        "Feline costume sample": "./halloween_images/feline.png",
        "Wizard costume sample": "./halloween_images/wizard.png",
        "Witch costume sample": "./halloween_images/witch.png",
        "Fairy costume sample": "./halloween_images/fairy.png"

    }
    
    global current_image ,converted_image_dict, image_label, image_status, current_label
    converted_image_dict = {}
    for name, path in image_dict.items():
        converted_image_dict[name] = ImageTk.PhotoImage((Image.open(path)).resize((600, 400)))

    global GalleryFrame
    GalleryFrame = LabelFrame(TableFrame) 
    GalleryFrame.pack()

    current_image = "Pirate costume sample"
    current_label = Label(GalleryFrame, text=current_image)
    current_label.pack()
   

    image_label = Label(GalleryFrame, image=converted_image_dict["Pirate costume sample"])
    image_label.pack()

    Description_frame = Frame(GalleryFrame)
    Description_frame.pack()
    image_status = Label(Description_frame, text="1 of" + ' ' + str(len(converted_image_dict)))
    image_status.grid(row=0, column=1)

    next_button = Button(Description_frame, text=">>>", command=lambda:showing_next(current_image), bg="Green", font="Bold")
    next_button.grid(row=0, column=2)
  
    previous_button = Button(Description_frame, text="<<<", command=lambda:showing_previous(current_image), bg="Green", font="Bold")
    previous_button.grid(row=0, column=0)


def showing_next(event=None):
        global current_image
        current_image_index = list(converted_image_dict.keys()).index(current_image)
        next_image_index = (current_image_index + 1) % len(converted_image_dict)
        current_image = list(converted_image_dict.keys())[next_image_index]
        image_label.config(image=converted_image_dict[current_image])
        image_status.config(text=str(next_image_index + 1) + ' ' + 'of' + ' ' + str(len(converted_image_dict)))
        current_label.config(text=current_image)


   

    
def showing_previous(event=None):
        global current_image
        current_image_index = list(converted_image_dict.keys()).index(current_image)
        previous_image_index = (current_image_index - 1) % len(converted_image_dict)
        current_image = list(converted_image_dict.keys())[previous_image_index]
        image_label.config(image=converted_image_dict[current_image])
        image_status.config(text=str(previous_image_index + 1) + ' ' + 'of' + ' ' + str(len(converted_image_dict)))
        current_label.config(text=current_image)





def update_costumetable():
    global recordframe01, recordframe02, recordframe03, recordframe04, recordframe05
    recordframe01 = Frame(TableFrame)
    recordframe01.grid(row=0, column=0)
    recordframe02 = Frame(TableFrame)
    recordframe02.grid(row=0, column=1)
    recordframe03 = Frame(TableFrame)
    recordframe03.grid(row=0, column=2)
    recordframe04 = Frame(TableFrame)
    recordframe04.grid(row=0, column=3)
    recordframe05 = Frame(TableFrame)
    recordframe05.grid(row=0, column=4)

    Tblhead01= Label(recordframe01, text="Id", font=('calibri & bold', 15))
    Tblhead01.pack()
    Tblhead02 = Label(recordframe02, text="Costume Name", font=('calibri & bold', 15))
    Tblhead02.pack()
    Tblhead03 = Label(recordframe03, text="Brand", font=('calibri & bold', 15))
    Tblhead03.pack()
    Tblhead04 = Label(recordframe04, text="Price($)", font=('calibri & bold', 15))
    Tblhead04.pack()
    Tblhead05 = Label(recordframe05, text="Quantity", font=('calibri & bold', 15))
    Tblhead05.pack()


    Database_connect()
    c.execute("SELECT * FROM costume")
    records = c.fetchall()
    for record in records:
        record01 = Label(recordframe01, text=str(record[0]), font=('calibri', 16))
        record01.pack()
        record02 = Label(recordframe02, text=str(record[1]), font=('calibri', 16))
        record02.pack()
        record03 = Label(recordframe03 ,text=str(record[2]), font=('calibri', 16))
        record03.pack()
        record04 = Label(recordframe04, text=str(record[3]), font=('calibri', 16))
        record04.pack()
        record05 = Label(recordframe05, text=str(record[4]), font=('calibri', 16))
        record05.pack()
    


DAYS = IntVar()
QUANTITY = IntVar()

def main_interface():
    
    global King_frame
    King_frame = Frame(root)
    King_frame.pack()


    wlcm_lbl= Label(King_frame, text="WELCOME TO HALLOWEEN RENTAL STORE", font=('calibri & Bold', 30), bg="Black",fg="white", bd=3)
    wlcm_lbl.pack()


    selection_frame= Frame(King_frame)
    selection_frame.pack()
    selection_lbl = Label(selection_frame, text="----------------------------------- Select your desired option -----------------------------------", font=('calibri', 20))
    selection_lbl.pack()


    radio_frame = Frame(King_frame)
    radio_frame.pack()
    global RadioValues
    RadioValues= IntVar()
    radio_button01 = Radiobutton(radio_frame, text="Rent costume\t", font=('calibri', 18),variable=RadioValues, value=1, command=selection)
    radio_button01.grid(row=0, column=0)
    radio_button02 = Radiobutton(radio_frame, text="Return costume\t", font=('calibri', 18),variable=RadioValues, value=2, command=selection)
    radio_button02.grid(row=0, column=1)
    radio_button03 = Radiobutton(radio_frame, text="Explore gallery", font=('calibri',18), variable=RadioValues, value=3, command=selection)
    radio_button03.grid(row=0, column=2)

    global selection_lblresult 
    selection_result_frame = Frame(King_frame)
    selection_result_frame.pack()
    selection_lblresult = Label(selection_result_frame, text="", font=('calibri', 15), )
    selection_lblresult.pack()


    global TableFrame
    TableFrame = LabelFrame(King_frame, text="Costume list", font=('calibri', 15),fg="blue", bd=3)
    TableFrame.pack()
    TableFrame.grid_columnconfigure(0, minsize=110, weight=1)
    TableFrame.grid_columnconfigure(1, minsize=140, weight=1)
    TableFrame.grid_columnconfigure(2, minsize=130, weight=1)
    TableFrame.grid_columnconfigure(3, minsize=100, weight=1)
    TableFrame.grid_columnconfigure(4, minsize=140, weight=1)
    
    update_costumetable()

    global dash_frame
    dash_frame = Frame(King_frame)
    dash_frame.pack()
    dash_label = Label(dash_frame, text="______________________________________________________________________", font=20)
    dash_label.pack()
    


    global Id, Quantity, Days, EntryFrame
    EntryFrame = Frame(King_frame)
    EntryFrame.pack()
    instructionframe = Frame(EntryFrame)
    instructionframe.pack()
    instruction_lbl = Label(instructionframe, text="Please enter valid Id no, quantity and days you want to rent or return", font=('calibri', 20))
    instruction_lbl.pack()
    inputframe = Frame(EntryFrame)
    inputframe.pack()
    Id_lbl = Label(inputframe, text="Id no.", font=('calibri', 18))
    Id_lbl.grid(row=0, column=0)
    Id = Entry(inputframe, font=('calibri', 15), state=DISABLED)
    Id.grid(row=0, column=1)
    Quantity_lbl = Label(inputframe, text="   Quantity", font=('calibri', 18))
    Quantity_lbl.grid(row=0, column=2)
    Quantity = Entry(inputframe, font=('calibri', 15), state=DISABLED, textvariable=QUANTITY)
    Quantity.grid(row=0, column=3)
    Days_lbl = Label(inputframe, text="   Days", font=('calibri', 18))
    Days_lbl.grid(row=0, column=4)
    Days = Entry(inputframe, font=('calibri',15), state=DISABLED, textvariable=DAYS)
    Days.grid(row=0, column=5)

    
    global result, resultframe
    resultframe = Frame(King_frame)
    resultframe.pack()
    result= Label(resultframe, text="", font=('calibri', 16))
    result.pack()

    global ButtonFrame
    ButtonFrame= Frame(King_frame)
    ButtonFrame.pack()
    rent_btn = Button(ButtonFrame, text="Rent", font=('calibri', 18), bg="green", width=20, command=lambda:MainEvent("Rent"))
    rent_btn.grid(row=0, column=0, padx=25, )
    return_btn = Button(ButtonFrame, text="Return", font=('calibri', 18), bg="green", width=20, command=lambda:MainEvent("Return") )
    return_btn.grid(row=0, column=1, padx=25)


    rentinvoice_btn = Button(ButtonFrame, text="Rent invoice", font=('calibri', 18), bg="green", width=20, command=lambda:invoice_processing("Rent invoice"))
    rentinvoice_btn.grid(row=1, column=0, padx=25, pady=10)
    returninvoice_btn = Button(ButtonFrame, text="Return invoice", font=('calibri', 18), bg = "green", width=20, command=lambda:invoice_processing("Return invoice"))
    returninvoice_btn.grid(row=1, column=1, padx=25)
 
    payment_btn = Button(ButtonFrame,text="Payment", font=('calibri',18), bg="green", width=20, command=Payment )
    payment_btn.grid(row=2, column=0)

    global filemenu01
    menubar = Menu(root)
    filemenu01 = Menu(menubar, tearoff=0)
    filemenu02 = Menu(menubar, tearoff=0)
    filemenu03 = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu01)
    filemenu01.add_command(label="Exit", command=Exit) 
    filemenu01.add_command(label="Save as txt", state=DISABLED)
    menubar.add_cascade(label="Home", command=main_interface_loop)
    menubar.add_cascade(label="Terms and Condition", menu=filemenu03)
    filemenu03.add_command(label="Rent:", font=("Bold", 11))
    filemenu03.add_command(label="One can rent as many costumes as desires. One have to return and pay")
    filemenu03.add_command(label="for each type of costume for having rent transaction again.")
    filemenu03.add_command(label="Return:", font=("Bold", 11))
    filemenu03.add_command(label="One can return each type of costume at any time, not more than days ")
    filemenu03.add_command(label="rented for. Otherwise, one have to pay extra charge for delay.")
    filemenu03.add_command(label="Payment:", font=("Bold", 11))
    filemenu03.add_command(label="One have to pay for each id costume separately. One can pay during")
    filemenu03.add_command(label="rent or return time.")
    filemenu03.add_command(label="Cost:", font=("Bold", 11))
    filemenu03.add_command(label="one have to pay the price of each quantity of each id costume.")
    filemenu03.add_command(label="Charge/Fee:", font=("Bold", 11))
    filemenu03.add_command(label="Maximum rent days is 5. If one rent for days greater than 5, one ")
    filemenu03.add_command(label="have to pay charge of 3$ for each extra day.")

    menubar.add_cascade(label="About", menu=filemenu02)
    filemenu02.add_command(label="This system is for renting and returning costumes")
    filemenu02.add_command(label="of Halloween rental store online.")
    root.config(menu=menubar)




def Exit():
    message = messagebox.askquestion('Halloween store', 'Are you sure you want to exit?')
    if message=='yes' :
        root.destroy()




def main_interface_loop():
    King_frame.destroy()
    main_interface()




root.mainloop()



















