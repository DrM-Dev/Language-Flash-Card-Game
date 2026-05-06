#====================IMPORTS:
from tkinter import *
import customtkinter
from PIL import ImageTk, Image

#====================Global Constants:
BACKGROUND_COLOR = "#B1DDC6"
LANG_TITLE_FONT = "Ariel", 40, "italic"
WORD_FONT = "Courier", 50, "bold"
#
# Buttons_FONT =

#====================SETUP
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
#-------------
root = customtkinter.CTk()
root.minsize(900,800)
root.maxsize(900,800)
root.config(padx=20,pady=20)
#-------------
root.title("Testing ground")
# window.iconbitmap()
#--------------------------
#-------------Widgets displacement
widgets_x_place = 20
widgets_y_place = 20
#|
widgets_x_displacement = 20
widgets_y_displacement = 20


#_____________________________________________________________
#0000-Button Test
####-------------------------BUTTON-ART / IMAGES
b1_normal_state_image = ImageTk.PhotoImage(Image.open("images/unclicked.png").resize((50,50)))
b1_hover_in_image = ImageTk.PhotoImage(Image.open("images/hovered.png").resize((50,50)))
b1_clicked_image =ImageTk.PhotoImage(Image.open("images/clicked.png").resize((50,50)))


####-------------------------BUTTON-MAIN-FUNCTIONS
def button_event():
    print("button pressed")


####-------------------------BUTTON-CONSTRUCTION Widget
button_1 = customtkinter.CTkButton(root, image=b1_normal_state_image , text="", height=50, width=50,command=button_event, fg_color="transparent",border_width=0, hover=False)
button_1.pack(padx=20,pady=20)


####-------------------------BUTTON-Aesthetic-functions
#----HOVER
def bt1_hover_in(event):
    button_1.configure(image=b1_hover_in_image)
def bt1_hover_out(event):
    button_1.configure(image=b1_normal_state_image)
#bind events:
button_1.bind("<Enter>", bt1_hover_in)
button_1.bind("<Leave>", bt1_hover_out)

#----CLICK-STATE
def bt1_clicked(event):
    button_1.configure(image=b1_clicked_image)
def bt1_unclicked(event):
    button_1.configure(image=b1_normal_state_image)
#bind events:
button_1.bind("<ButtonPress-1>", bt1_clicked)
button_1.bind("<ButtonRelease-1>", bt1_unclicked)


#_____________________________________________________________





#==============END
root.mainloop()
