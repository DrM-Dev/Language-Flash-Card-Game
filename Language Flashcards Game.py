#Language Flashcards Game - ver       by      Dr.M-Dev
import random

ver = 0.1
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
lang_title = "French"
player_choice = None
player_SCORE = 0
score_effected = False #(false -> the score is NOT YET Effected),
                      # (true -> the score have already been effected, and shouldn't be altered any further)
#
# fetched_tuple = None
the_word = "word_null"
the_meaning = ""
#
lang_keys_list = []
guessed_keys_list = []

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
#################################################################CHECKING PLAYER GUESS / WORD-CARD SWITCH MECHANIC
def check_player_answer():
    global player_choice
    global player_SCORE
    #
    global score_effected
    # -------------------
    # global fetched_tuple
    global the_word
    global the_meaning
    # ++++
    global guessed_keys_list
    # -------------------
    # -------------------
    answer_state = False
    #~~~~~~~~~~~~~~~~~~~~~~~~
    #~~~~~~~~~~~~~~~~~~~~~~~~fixing playing mechanic (also no need for score system, yet I will keep it) <!>
    if player_choice: #and fetched_tuple[1] == the_meaning:
        answer_state = True
    # if not player_choice and the_word != the_meaning:
    #     answer_state = True
    #-----
    # if player_choice and the_word != the_meaning:
    #     answer_state = False
    if not player_choice: #and fetched_tuple[1] == the_meaning:
        answer_state = False
    # ~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~~~~~~~~~~~~~
    if answer_state:
        guessed_keys_list.append(the_word)
        #-----------
        if not score_effected:
            player_SCORE += 1
            score_effected = True
        #
        # switch_card_back() -> IF YOU KNOW THE MEANING...THEN TIME TO PULL ANOTHER CARD:
        picking_word()
        #>activate the (pick another card) -> picking_word() ---> it will do the switch_card_front() AUTOMATICALLY
        # ------------------------------
        print("DEBUG ->>>>> CORRECT ANSWER :D")
        print(f"SCORE-> {player_SCORE}")
        print(f"\nGUESSED LIST:\n{guessed_keys_list}")
        # ------

        ####
    elif not answer_state:
        if not score_effected:
            player_SCORE -= 1
            score_effected = True
        #
        switch_card_back()
        #----------------
        # picking_word() #FLIP A NEW CARD!
        # ------------------------------
        print("DEBUG ->>>>> WRONG ANSWER :(")
        print(f"SCORE-> {player_SCORE}")
        print(f"\nGUESSED LIST:\n{guessed_keys_list}")
        # ------


#_________________________________________________________PICKING RANDOM WORD:
list_obtained = False
def match_lang_keys_lists():
    global lang_keys_list
    #global guessed_keys_list
    #=================
    #=================
    lang_keys_list = lang_csv_reader.lang_keys_list
    # DEBUG:
    # print(f"list fetched ->{lang_keys_list}")
    # print(f"{guessed_keys_list}")

#++++++++++++++++++++++++++++++
def picking_word():
    # global fetched_tuple
    global the_word
    global the_meaning
    #++++
    global guessed_keys_list
    #=================
    #=================NEW:
    if not list_obtained:
        match_lang_keys_lists()
    #----------------
    global score_effected
    score_effected = False
    #=================
    #=================
    random_word_tuple = lang_csv_reader.pick_random_word(guessed_keys_list)
    #
    # fetched_tuple = random_word_tuple
    try:
        the_word = random_word_tuple[0]
        the_meaning = random_word_tuple[1]
        print(f"\nTHE TUPLE +++++++++++++++++[+]+++++++++++++++++++. {random_word_tuple}")
    except IndexError:
        print(f"\nTHE TUPLE ---------------[X]---------------------. {random_word_tuple}")
        picking_word()
    #=================
    #=================
    switch_card_front()
    # DEBUG:
    # print(f"THE WORD{the_word}\nANDDDD IT'S MEANING IS {the_meaning}")

#--------------
#GET A CARD BUTTON
flip_front_button = customtkinter.CTkButton(root, text="GET A NEW CARD", height=50, width=50,command=picking_word, bg_color="white", text_color="White", font=("Courier", 15, "bold"))
flip_front_button.place(x=300,y=500)










#====================================================================================================UIs + More
card_facing = "front" #only 2 states, #front/#back
def check_state():
    global card_facing
    global lang_title
    ####
    global the_word
    global the_meaning
    ####
    if card_facing == "front":
        main_canvas.configure(bg="white")
        #
        main_canvas.itemconfig(lang_title_text, text=f"{lang_title}") #ASKING ABOUT THE WORD
        main_canvas.itemconfig(random_word_text, text=f"{the_word}")
        #
        card_widget.configure(image=card_FRONT_img)
        #==========================================
    elif card_facing == "back":
        main_canvas.configure(bg="#86C1B0")
        #
        main_canvas.itemconfig(lang_title_text, text="Meaning:") #SHOWING THE MEANING
        main_canvas.itemconfig(random_word_text, text=f"{the_meaning}")
        #
        card_widget.configure(image=card_BACK_img)
#------------------------------------------
def switch_card_front():
    global card_facing
    card_facing = "front"
    print("debug: switch front")
    #
    check_state()
#----
def switch_card_back():
    global card_facing
    card_facing = "back"
    print("debug: switch back")
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
# the_word = "word_null" (a global variable)
lang_title_text = main_canvas.create_text(700/2,100, text=f"{lang_title}", font=LANG_TITLE_FONT)
random_word_text = main_canvas.create_text(700/2,280, text=f"{the_word}", font=WORD_FONT)





#_____________________________________________________________BUTTONS
#0000-CHECK-MARK Button
####-------------------------BUTTON-ART / IMAGES
correct_b__normal_state_image = customtkinter.CTkImage(light_image=Image.open("images/right_norm.png"),size=(100, 100))
correct_b__hover_in_image = customtkinter.CTkImage(light_image=Image.open("images/right_hover.png"),size=(100, 100))
correct_b__clicked_image = customtkinter.CTkImage(light_image=Image.open("images/right_clicked.png"),size=(100, 100))

####-------------------------BUTTON-MAIN-FUNCTIONS
def check_button_event():
    global player_choice
    global guessed_keys_list
    #
    player_choice = True
    #-------------------
    #debug
    print("CORRECT pressed")
    #-------------------
    check_player_answer()


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
    player_choice = False
    # -------------------
    # debug
    print("WRONG pressed")
    # -------------------
    check_player_answer()

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


#_____________________________________________________________Starting the code with:
picking_word()




#==============END
root.mainloop()
