from tkinter import *
from PIL import Image, ImageTk
from main_interface import recordframe01, recordframe02, recordframe03, recordframe04, recordframe05, TableFrame, dash_frame, EntryFrame, resultframe, ButtonFrame
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