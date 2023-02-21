from tkinter import *
from PIL import Image, ImageTk
import sqlite3

root = Tk()
root.title("Login_register prototype")
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
            lbl_result1.config(text="Successfully Logged In", fg="green", font=('calibri', 15))
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
    # main_interface()

root.mainloop()
