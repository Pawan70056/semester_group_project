from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk

win = Tk()
win.title("Database_handling")
icon = PhotoImage(file="./icon/database01.png")
win.iconphoto("peaky", icon)



width = 1250
height = 760
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
win.geometry("%dx%d+%d+%d" % (width, height, x, y))



image01 = ImageTk.PhotoImage((Image.open("./icon/database02.png")).resize((400, 450)))
img_lbl01 = Label(win, image=image01)
img_lbl01.place(x=650, y=50)



beting_caption = Label(win, text="Tech makes us strong\nIdeas for life\nA greater measure of confidence\nWe are here to change the world\nTechnology for innovators\nTechnology made with trust\nConnection with people\nEmpowered by innovation", font=("calibri",25))
beting_caption.place(x=1100, y=110)



def Database_Create():
    global create, cursor
    create = sqlite3.connect("Database.db")
    cursor = create.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `costume` (Costume_Id TEXT, Costume_Name TEXT, Brand TEXT, Price TEXT, Quantity TEXT )")



ID = StringVar()
COSTUMENAME = StringVar()
BRAND = StringVar()
PRICE = StringVar()
QUANTITY = StringVar()
CHOOSEID = StringVar()



# creating labels
caption_lbl = Label(win, text="We developers love handling data!!", font=('calibri & Bold', 25), fg="red")
caption_lbl.place(x=60, y=70)

Id_lbl = Label(win, text="Costume Id", font=('calibri',20))
Id_lbl.place(x=90, y=120)

CostumeName_lbl = Label(win, text="Costume Name", font=('calibri', 20))
CostumeName_lbl.place(x=70, y=150)

Brand_lbl = Label(win, text="Brand", font=('calibri', 20))
Brand_lbl.place(x=118, y=180)

Price_lbl = Label(win, text="Price", font=('calibri', 20))
Price_lbl.place(x=118, y=210)

Quantity_lbl = Label(win, text="Quantity", font=('calibri', 20))
Quantity_lbl.place(x=100, y=240)



# creating text boxes for labels
Id = Entry(win, font=('calibri', 15), textvariable=ID)
Id.place(x=300, y=122)

CostumeName = Entry(win, font=('calibri', 15), textvariable=COSTUMENAME)
CostumeName.place(x=300, y=154)

Brand = Entry(win, font=('calibri', 15), textvariable=BRAND)
Brand.place(x=300, y=185)

Price = Entry(win, font=('calibri', 15), textvariable=PRICE)
Price.place(x=300, y=215)

Quantity = Entry(win, font=('calibri', 15), textvariable=QUANTITY)
Quantity.place(x=300, y=246)



# creating textbox for chooseId
Choose_Box = Entry(win, font=('calibri', 15), textvariable=CHOOSEID)
Choose_Box.place(x=300, y=424)

Choose_Box_lbl = Label(win, text="Choose Id", font=('calibri', 20))
Choose_Box_lbl.place(x=160, y=420)



def InsertIntoTable():  
    entry1 = COSTUMENAME.get()
    entry2 = BRAND.get()
    entry3 = PRICE.get()
    entry4 = QUANTITY.get()
    entry5 = ID.get()

    if (entry1.isspace() or entry1=="") or (entry2.isspace() or entry2=="") or (entry3.isspace() or entry3=="") or (entry4.isspace() or entry4=="") or (entry5.isspace() or entry5==""):
        messagebox.showerror('error', "all fields are required")
    else:
        Database_Create()
        cursor.execute("INSERT INTO `costume` (Costume_Id, Costume_Name, Brand, Price, Quantity) VALUES(?, ?, ?, ?, ?)", (str(ID.get()), str(COSTUMENAME.get()), str(BRAND.get()), str(PRICE.get()), str(QUANTITY.get())))
        create.commit()
        create.close()
        messagebox.showinfo('costume', "Inserted successfully")



Submit_btn = Button(win, text="Submit", font=('calibri & bold', 18), bg="pale green", width=20, command=InsertIntoTable)
Submit_btn.place(x=320, y=285)



def ClearEntries():
    ID.set("")
    COSTUMENAME.set("")
    BRAND.set("")
    PRICE.set("")
    QUANTITY.set("")



Add_record_btn = Button(win, text="Add record", width=20, font=('calibri & bold', 18), bg="aqua", command=ClearEntries)
Add_record_btn.place(x=320, y=340)



def EditID():
    global entry
    entry = CHOOSEID.get()
    if entry.isspace() or entry=="":
        messagebox.showerror('error', "'Choose Id'!^empty^")
    else:
        global editor
        editor = Toplevel()
        editor.title("Data Editor")
        icon2 = PhotoImage(file="./icon/editor.png")
        editor.iconphoto("Blinders", icon2)
        

        width = 600
        height = 500
        screen_width = editor.winfo_screenwidth()
        screen_height = editor.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        editor.geometry("%dx%d+%d+%d" % (width, height, x, y))
                
        
        caption_lbl02 = Label(editor, text="We don't worry, we update regularly", font=('calibri', 25), fg="red")
        caption_lbl02.place(x=60, y=70)
        
        Id_lbl = Label(editor, text="Costume Id", font=('calibri', 20))
        Id_lbl.place(x=90, y=120)

        CostumeName_lbl = Label(editor, text="Costume Name", font=('calibri', 20))
        CostumeName_lbl.place(x=70, y=150)

        Brand_lbl = Label(editor, text="Brand", font=('calibri', 20))
        Brand_lbl.place(x=118, y=180)

        Price_lbl = Label(editor, text="Price", font=('calibri', 20))
        Price_lbl.place(x=118, y=210)

        Quantity_lbl = Label(editor, text="Quantity", font=('calibri', 20))
        Quantity_lbl.place(x=100, y=240)


        global Id_editor, CostumeName_editor, Brand_editor, Price_editor, Quantity_editor
        Id_editor = Entry(editor, font=('calibri', 15))
        Id_editor.place(x=300, y=122)

        CostumeName_editor = Entry(editor, font=('calibri', 15))
        CostumeName_editor.place(x=300, y=154)

        Brand_editor = Entry(editor, font=('calibri', 15))
        Brand_editor.place(x=300, y=185)

        Price_editor = Entry(editor, font=('calibri', 15))
        Price_editor.place(x=300, y=215)

        Quantity_editor = Entry(editor, font=('calibri', 15), )
        Quantity_editor.place(x=300, y=246)


        Database_Create()
        cursor.execute("SELECT * FROM costume WHERE `Costume_Id`=" + CHOOSEID.get())
        records = cursor.fetchall()
        for record in records:
            Id_editor.insert(0, record[0])
            CostumeName_editor.insert(0, record[1])
            Brand_editor.insert(0, record[2])
            Price_editor.insert(0, record[3])
            Quantity_editor.insert(0, record[4])


        save_button = Button(editor, text="Save", width=20, bg="skyblue", font=('calibri', 18), command=UpdateId)
        save_button.place(x=155, y=290)

        exit_button = Button(editor, text="Exit", width=20, font=('calibri', 18), bg="red", command=exit)
        exit_button.place(x=155, y=345)



def UpdateId():
    Database_Create()
    cursor.execute("""UPDATE costume SET Costume_Id=:med1, Costume_Name=:med2, Brand=:med3, Price=:med4, Quantity=:med5 WHERE Costume_Id=:id""", {'med1':Id_editor.get() ,'med2':CostumeName_editor.get(), 'med3':Brand_editor.get(), 'med4':Price_editor.get(), 'med5':Quantity_editor.get(), 'id':Choose_Box.get()})
    create.commit()
    create.close()

    messagebox.showinfo('costume', "Updated successfully")
    CHOOSEID.set("")

    editor.destroy()



Update_record_btn = Button(win, text="Update", font=('calibri & bold', 18), width=20, bg="skyblue", command=EditID)
Update_record_btn.place(x=60, y=520)



def Trash():
    entry5 = CHOOSEID.get()
    if entry5.isspace() or entry5=="":
        messagebox.showerror('error', "'Choose Id'!^empty^")
    else:
        global response
        response = messagebox.askyesno('costume', "Are you sure you want to delete?")
        if response==1:
            Database_Create()
            cursor.execute("DELETE FROM costume WHERE Costume_Id=" + CHOOSEID.get())
            create.commit()
            create.close()

            messagebox.showinfo('costume', "Deleted successfully")
            CHOOSEID.set("")




Delete_record_btn = Button(win, text="Delete", font=('calibri & Bold', 18), width=20, bg="red", command=Trash)
Delete_record_btn.place(x=60, y=580)



def ShowRecord():
    Database_Create()
    cursor.execute("SELECT * FROM costume")
    records = cursor.fetchall()
    print_records = ""
    for record in records:
        print_records += str(record[0]) + "    " + str(record[1]) + "    " + str(record[2]) + "    " + str(record[3]) + "    " + str(record[4]) + "\n"

    show_lblframe = LabelFrame(win, text="Records", font=('calibri & bold',18), fg="red", padx=5, pady=5)
    show_lblframe.place(x=370, y=530)

    printing_records = Label(show_lblframe, text=print_records, font=('calibri', 16), fg="green" )
    printing_records.pack(side=LEFT)

    Show_record_btn.config(text="Hide/update record", command=lambda:HideRecord(show_lblframe))



def HideRecord(show_lblframe):
    show_lblframe.destroy()
    Show_record_btn.config(text="Show record" , command=ShowRecord)



Show_record_btn = Button(win, text="Show record", font=('calibri & bold', 18), width=20, bg="yellow", command=ShowRecord)
Show_record_btn.place(x=320, y=470)


win.mainloop()



