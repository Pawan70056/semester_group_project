from tkinter import *
import sqlite3
from tkinter import messagebox


root=Tk()
root.title("Main Interface Prototype")
root_icon = PhotoImage(file="./icon/pumpkin.png")
root.iconphoto("Feary Pumpkin", root_icon)


width = 1250
height = 900
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))



def Exit():
    message = messagebox.askquestion('Halloween store', 'Are you sure you want to exit?')
    if message=='yes' :
        root.destroy()



def main_interface_loop():
    King_frame.destroy()
    main_interface()



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


    conn = sqlite3.connect("Database.db")
    c = conn.cursor()

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
    

    
    dash_frame = Frame(King_frame)
    dash_frame.pack()
    dash_label = Label(dash_frame, text="______________________________________________________________________", font=20)
    dash_label.pack()
    


    global Id, Quantity, Days
    EntryFrame = Frame(King_frame)
    EntryFrame.pack()
    instructionframe = (EntryFrame)
    instructionframe.pack(anchor=W)
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



    global result
    resultframe = Frame(King_frame)
    resultframe.pack()
    result= Label(resultframe, text="", font=('calibri', 16))
    result.pack()




    ButtonFrame= Frame(King_frame)
    ButtonFrame.pack()
    rent_btn = Button(ButtonFrame, text="Rent", font=('calibri', 18), bg="green", width=20,)
    rent_btn.grid(row=0, column=0, padx=25, )
    return_btn = Button(ButtonFrame, text="Return", font=('calibri', 18), bg="green", width=20,  )
    return_btn.grid(row=0, column=1, padx=25)




    rentinvoice_btn = Button(ButtonFrame, text="Rent invoice", font=('calibri', 18), bg="green", width=20, )
    rentinvoice_btn.grid(row=1, column=0, padx=25, pady=10)
    returninvoice_btn = Button(ButtonFrame, text="Return invoice", font=('calibri', 18), bg = "green", width=20, )
    returninvoice_btn.grid(row=1, column=1, padx=25)
 


    payment_btn = Button(ButtonFrame,text="Payment", font=('calibri',18), bg="green", width=20, )
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



main_interface()



root. mainloop()