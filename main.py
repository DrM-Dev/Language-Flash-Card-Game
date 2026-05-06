#====================IMPORTS:
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTkImage
#
import lang_csv_reader

#====================Global Constants:
BACKGROUND_COLOR = "#B1DDC6"
LANG_TITLE_FONT = "Ariel", 40, "italic"
WORD_FONT = "Courier", 50, "bold"

#====================Globals:
player_choice = None
random_word = "word_null"

#====================SETUP
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
#-------------
root = customtkinter.CTk()
#
window_width = 900
window_height = 600
#
root.minsize(window_width,window_height)
root.maxsize(window_width,window_height)
root.config(padx=20,pady=20)
#-------------
root.title("Testing ground")
# window.iconbitmap()
#--------------------------
#-------------Widgets displacement
widgets_x_place = 20
widgets_y_place = 20
#|
buttons_x_displacement = 20
buttons_y_displacement = 50







#====================================================================================================Flash Cards System
def pick_a_word():
    global random_word
    #
    random_word = lang_csv_reader.pick_random_word()
    #
    main_canvas.itemconfig(random_word_text, text=f"{random_word}")


#====================================================================================================UIs
card_facing = "front" #only 2 states, #front/#back
def check_state():
    global card_facing
    ####
    if card_facing == "front":
        main_canvas.configure(bg="white")
        card_widget.configure(image=card_FRONT_img)
    elif card_facing == "back":
        main_canvas.configure(bg="#86C1B0")
        card_widget.configure(image=card_BACK_img)
#------------------------------------------
def switch_card_front():
    global card_facing
    card_facing = "front"
    #
    check_state()
#----
def switch_card_back():
    global card_facing
    card_facing = "back"
    #
    check_state()

#_____________________________________________________________Labels + more
#0000-Card
# FRONT_card_body_img = CTkImage(light_image=Image.open("images/card_front.png"), size=(800,500))
card_FRONT_img = customtkinter.CTkImage(light_image=Image.open("images/card_front.png"),size=(700,400))
card_BACK_img = customtkinter.CTkImage(light_image=Image.open("images/card_back.png"),size=(700,400))

#_________________LABEL-IMAGE
card_widget = customtkinter.CTkLabel(root, image=card_FRONT_img, text="")
card_widget.place(x=window_width/2-360, y=window_height/4-120)

#_________________Canvas
# highlightthickness=0 keeps it looking modern without a clunky border
main_canvas = Canvas(root, width=700, height=400, highlightthickness=0, bg="white")
main_canvas.place(x=window_width/2-260, y=window_height/4-90)
####
#Canva-Text:
# random_word = "word_null" (a global variable)
lang_title_text = main_canvas.create_text(700/2,100, text="Fwench :3", font=LANG_TITLE_FONT)
random_word_text = main_canvas.create_text(700/2,280, text=f"{random_word}", font=WORD_FONT)





#_____________________________________________________________BUTTONS
#0000-CHECK-MARK Button
####-------------------------BUTTON-ART / IMAGES
correct_b__normal_state_image = customtkinter.CTkImage(light_image=Image.open("images/right_norm.png"),size=(100, 100))
correct_b__hover_in_image = customtkinter.CTkImage(light_image=Image.open("images/right_hover.png"),size=(100, 100))
correct_b__clicked_image = customtkinter.CTkImage(light_image=Image.open("images/right_clicked.png"),size=(100, 100))

####-------------------------BUTTON-MAIN-FUNCTIONS
def check_button_event():
    global player_choice
    player_choice = True
    #debug
    print("CORRECT pressed")


####-------------------------BUTTON-CONSTRUCTION Widget
check_mark_button = customtkinter.CTkButton(root, image=correct_b__normal_state_image , text="", height=50, width=50,command=check_button_event, fg_color="transparent",border_width=0, hover=False)
check_mark_button.place(x=150,y=400+buttons_y_displacement)

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
#0000-WRONG-CLICK Button
####-------------------------BUTTON-ART / IMAGES
wrong_b__normal_state_image = customtkinter.CTkImage(light_image=Image.open("images/wrong_norm.png"),size=(100, 100))
wrong_b__hover_in_image = customtkinter.CTkImage(light_image=Image.open("images/wrong_hover.png"),size=(100, 100))
wrong_b__clicked_image = customtkinter.CTkImage(light_image=Image.open("images/wrong_clicked.png"),size=(100, 100))

####-------------------------BUTTON-MAIN-FUNCTIONS
def wrong_button_event():
    global player_choice
    player_choice = True
    # debug
    print("WRONG pressed")

####-------------------------BUTTON-CONSTRUCTION Widget
wrong_button = customtkinter.CTkButton(root, image=wrong_b__normal_state_image , text="", height=50, width=50,command=wrong_button_event, fg_color="transparent",border_width=0, hover=False)
wrong_button.place(x=600,y=400+buttons_y_displacement)

####-------------------------BUTTON-Aesthetic-functions
#----HOVER
def wrong_b_hover_in(event):
    wrong_button.configure(image=wrong_b__hover_in_image)
def wrong_b_hover_out(event):
    wrong_button.configure(image=wrong_b__normal_state_image)
#bind events:
wrong_button.bind("<Enter>", wrong_b_hover_in)
wrong_button.bind("<Leave>", wrong_b_hover_out)

#----CLICK-STATE
def wrong_b_clicked(event):
    wrong_button.configure(image=wrong_b__clicked_image)
def wrong_b_unclicked(event):
    wrong_button.configure(image=wrong_b__normal_state_image)
#bind events:
wrong_button.bind("<ButtonPress-1>", wrong_b_clicked)
wrong_button.bind("<ButtonRelease-1>", wrong_b_unclicked)


#_____________________________________________________________





#==============END
root.mainloop()
