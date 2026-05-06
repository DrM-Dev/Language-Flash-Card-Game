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
#0000-CHECK-MARK Button
####-------------------------BUTTON-ART / IMAGES
correct_b__normal_state_image = customtkinter.CTkImage(light_image=Image.open("images/right_norm.png"),size=(100, 100))
correct_b__normal_state_image = customtkinter.CTkImage(light_image=Image.open("images/right_norm.png"),size=(100, 100))
correct_b__normal_state_image = customtkinter.CTkImage(light_image=Image.open("images/right_norm.png"),size=(100, 100))
#
# correct_b__normal_state_image = ImageTk.PhotoImage(Image.open("images/right_norm.png").resize((100,100)))
# correct_b__hover_in_image = ImageTk.PhotoImage(Image.open("images/right_hover.png").resize((100,100)))
# correct_b__clicked_image =ImageTk.PhotoImage(Image.open("images/right_clicked.png").resize((100,100)))


####-------------------------BUTTON-MAIN-FUNCTIONS
def button_event():
    print("button pressed")


####-------------------------BUTTON-CONSTRUCTION Widget
check_mark_button = customtkinter.CTkButton(root, image=correct_b__normal_state_image , text="", height=50, width=50,command=button_event, fg_color="transparent",border_width=0, hover=False)
check_mark_button.pack(padx=20,pady=20)


####-------------------------BUTTON-Aesthetic-functions
#----HOVER
def check_b_hover_in(event):
    check_mark_button.configure(image=correct_b__hover_in_image)
def check_b_hover_out(event):
    check_mark_button.configure(image=correct_b__normal_state_image)
#bind events:
check_mark_button.bind("<Enter>", check_b_hover_in)
check_mark_button.bind("<Leave>", check_b_hover_out)

#----CLICK-STATE
def check_b_clicked(event):
    check_mark_button.configure(image=correct_b__clicked_image)
def check_b_unclicked(event):
    check_mark_button.configure(image=correct_b__normal_state_image)
#bind events:
check_mark_button.bind("<ButtonPress-1>", check_b_clicked)
check_mark_button.bind("<ButtonRelease-1>", check_b_unclicked)


#_____________________________________________________________





#==============END
root.mainloop()
