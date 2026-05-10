#Language Flashcards Game - ver       by      Dr.M-Dev
ver = "0.1.1"
#====================IMPORTS:
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTkImage, CTkLabel
#
import lang_csv_reader
import random

#====================Global Constants:
BACKGROUND_COLOR = "#B1DDC6"
LANG_TITLE_FONT = "Ariel", 40, "italic"
WORD_FONT = "Courier", 50, "bold"

#====================Globals:
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
root.configure(fg_color=BACKGROUND_COLOR)
#
window_width = 1000
window_height = 600
#
root.minsize(window_width,window_height)
root.maxsize(window_width,window_height)
root.config(padx=20,pady=20)
#-------------
root.title(f"Language Flashcards Game {ver}")
#----
root.iconbitmap("images/LangaugeFlashGame_bitmap.ico")
#--------------------------
#-------------Widgets displacement
widgets_x_place = 20
widgets_y_place = 20
#|
buttons_x_displacement = 50
buttons_y_displacement = 50


#====================#====================#====================#==================
#====================#====================#====================#====================LANGUAGES Globals:
#====================#====================#====================#==================
#LANGAUGES
FRENCH_LANG = "French"
# FRENCH_LANG_ICON =
#x+x+x+x+x+x+x+x+x+x+x+x
chosen_lang = "French" #default
#x+x+x+x+x+x+x+x+x+x+x+x
lang_title = chosen_lang

# def lang_selected():
#     global chosen_lang
#     global lang_title
#     #


#++++++++++++++++++++++++++++++++++++++++BUTTON & FUNCTIONS
LP_Window_Is_ON = False #Disabled by default! #that way you can "HOVER and ACTIVATE IT"
#+++++++++++++++++++#
#______________________SWITCHING FUN\\
def pick_this_language(language):
    global chosen_lang
    global lang_title
    #----
    if language == "French":
        chosen_lang = "French"
        lang_title = chosen_lang
    elif language == "German":
        chosen_lang = "German"
        lang_title = chosen_lang
    elif language == "Russian":
        chosen_lang = "Russian"
        lang_title = chosen_lang
    elif language == "Spanish":
        chosen_lang = "Spanish"
        lang_title = chosen_lang
    elif language == "Chinese":
        chosen_lang = "Chinese"
        lang_title = chosen_lang
    else:
        chosen_lang = "French"
        lang_title = chosen_lang
    #----
    lang_csv_reader.lang_switch_db(chosen_lang)
    print(f"\n<!>--> Language Database Switched to {chosen_lang}")
#+++++++++++++++++++#

#__________________BUTTONS FUN\\ #French or German or Russian or Spanish or Chinese
def select_french():
    pick_this_language("French")
def select_german():
    pick_this_language("German")
def select_russian():
    pick_this_language("Russian")
def select_spanish():
    pick_this_language("Spanish")
def select_chinese():
    pick_this_language("Chinese")

#__________________MAIN FUN\\
def pick_language():
    ##################STARTUP
    global LP_Window_Is_ON
    LP_Window_Is_ON = True #-->#IMPORTANT SWITCH (to disable click-ablity & hover images)\\
    # {-} #
    print("DEBUG: pick-language window activated")
    print(f"LANG PICK WINDOW STATE->>{LP_Window_Is_ON}")
    switchL_mark_button.configure(image=switchL_b__disabled_image)
    switchL_mark_button.configure(state="disabled")

    ##################SETUP:
    # ================
    # ================
    pick_lang_window = customtkinter.CTkToplevel(root)
    pick_lang_window.iconbitmap("images/LangaugeFlashGame_bitmap.ico")
    pick_lang_window.attributes("-topmost", True)
    #
    pick_lang_window.configure(fg_color=BACKGROUND_COLOR)
    #
    pick_lang_window.minsize(500, 400)
    pick_lang_window.maxsize(500, 400)
    pick_lang_window.config(padx=20, pady=20)
    # -------------
    pick_lang_window.title(f"Select A Language :)")
    # ----
    # #NOW switching this window to TOP LEVEL so it can respond to commands
    # print(" <!> WINDOW-2 is top level now <!>")
    # customtkinter.CTkToplevel(master=pick_lang_window)
    # ================
    # ================

    ###################Pick Language Window Options: #French or German or Russian or Spanish or Chinese
    #Language Image files:
    french_lang_flag_img = customtkinter.CTkImage(light_image=Image.open("images/Flags/fr_flag.png"),size=(100,50))
    german_lang_flag_img = customtkinter.CTkImage(light_image=Image.open("images/Flags/de_flag.png"), size=(100, 50))
    russian_lang_flag_img = customtkinter.CTkImage(light_image=Image.open("images/Flags/ru_flag.png"), size=(100, 50))
    spanish_lang_flag_img = customtkinter.CTkImage(light_image=Image.open("images/Flags/es_sp_flag.png"), size=(100, 50))
    chinese_lang_flag_img = customtkinter.CTkImage(light_image=Image.open("images/Flags/zh_ch_flag.png"), size=(100, 50))

    ###################
    french_lang_flag_b = customtkinter.CTkButton(pick_lang_window, image=french_lang_flag_img, text="", height=50,
                                               width=100,
                                               command=select_french, fg_color="transparent",
                                               bg_color="transparent", border_width=0, hover_color="white")
# ----
    german_lang_flag_b = customtkinter.CTkButton(pick_lang_window, image=german_lang_flag_img, text="", height=50,
                                               width=100,
                                               command=select_german, fg_color="transparent",
                                               bg_color="transparent", border_width=0, hover_color="white")
#----
    russian_lang_flag_b = customtkinter.CTkButton(pick_lang_window, image=russian_lang_flag_img, text="", height=50,
                                               width=100,
                                               command=select_russian, fg_color="transparent",
                                               bg_color="transparent", border_width=0, hover_color="white")
#----
    spanish_lang_flag_b = customtkinter.CTkButton(pick_lang_window, image=spanish_lang_flag_img, text="", height=50,
                                               width=100,
                                               command=select_spanish, fg_color="transparent",
                                               bg_color="transparent", border_width=0, hover_color="white")
#----
    chinese_lang_flag_b = customtkinter.CTkButton(pick_lang_window, image=chinese_lang_flag_img, text="", height=50,
                                               width=100,
                                               command=select_chinese, fg_color="transparent",
                                               bg_color="transparent", border_width=0, hover_color="white")
#------------------------------------
    flags_x_place = 50
    flags_y_place = -60
    flags_displacement = 60
    #--
    french_lang_flag_b.place(x=flags_x_place,y=flags_y_place+flags_displacement*1)
    german_lang_flag_b.place(x=flags_x_place,y=flags_y_place+flags_displacement*2)
    russian_lang_flag_b.place(x=flags_x_place,y=flags_y_place+flags_displacement*3)
    spanish_lang_flag_b.place(x=flags_x_place,y=flags_y_place+flags_displacement*4)
    chinese_lang_flag_b.place(x=flags_x_place,y=flags_y_place+flags_displacement*5)

#------------------------------------ [More Labels:] ------------------------------------
    # Language Labels
    language_label_fonts = ("Courier", 40, "bold")
    # French or German or Russian or Spanish or Chinese
    french_lang_label = customtkinter.CTkLabel(pick_lang_window ,text="French",text_color="black" ,font=language_label_fonts,fg_color="transparent", bg_color="transparent")
    french_lang_label.place(x=flags_x_place + 150,y=flags_y_place+flags_displacement * 1 + 8)
    #
    german_lang_label = customtkinter.CTkLabel(pick_lang_window, text="German", text_color="black",font=language_label_fonts, fg_color="transparent", bg_color="transparent")
    german_lang_label.place(x=flags_x_place + 150, y=flags_y_place + flags_displacement * 2 + 8)
    #
    russian_lang_label = customtkinter.CTkLabel(pick_lang_window, text="Russian", text_color="black",font=language_label_fonts, fg_color="transparent", bg_color="transparent")
    russian_lang_label.place(x=flags_x_place + 150, y=flags_y_place + flags_displacement * 3 + 8)
    #
    spanish_lang_label = customtkinter.CTkLabel(pick_lang_window, text="Spanish", text_color="black",font=language_label_fonts, fg_color="transparent", bg_color="transparent")
    spanish_lang_label.place(x=flags_x_place + 150, y=flags_y_place + flags_displacement * 4 + 8)
    #
    chinese_lang_label = customtkinter.CTkLabel(pick_lang_window, text="Chinese", text_color="black",font=language_label_fonts, fg_color="transparent", bg_color="transparent")
    chinese_lang_label.place(x=flags_x_place + 150, y=flags_y_place + flags_displacement * 5 + 8)


#__________________________________________________
    ################## LANGUAGE-WINDOW-OPTIONS END:
    def on_closing():
        global LP_Window_Is_ON
        LP_Window_Is_ON = False #-->#IMPORTANT SWITCH (to enable click-ablity & hover images)\\
        # {-} #
        print("DEBUG: pick-language window IS OFF")
        print(f"LANG PICK WINDOW STATE->>{LP_Window_Is_ON}")
        switchL_mark_button.configure(image=switchL_b__normal_state_image)
        switchL_mark_button.configure(state="normal")
        #
        #
        # print("<!> switching back to the main window! <!>") #--->NO NEED, only .destroy() :)
        # customtkinter.CTkToplevel(master=root)
        pick_lang_window.destroy()  # Explicitly close the window

    pick_lang_window.protocol("WM_DELETE_WINDOW", on_closing)
    ################END_mainloop:
    pick_lang_window.mainloop()





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
            score_counter.configure(text=f"Score:{player_SCORE}")
            ##
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
            if player_SCORE != 0:
                player_SCORE -= 1
            #---
            score_counter.configure(text=f"Score:{player_SCORE}")
            ##
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
#GET A CARD BUTTON - Terminal / Primordial-Button xD
# flip_front_button = customtkinter.CTkButton(root, text="GET A NEW CARD", height=50, width=50,command=picking_word, bg_color="white", text_color="White", font=("Courier", 15, "bold"))
# flip_front_button.place(x=300,y=500)
# [edit: I decided to make it into a new feature "a fully functional button with CTk]




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

#_________________LABEL-TEXT (for player score)
score_counter = customtkinter.CTkLabel(root, text=f"Score:{player_SCORE}", font=("Courier", 30, "bold"), text_color="black")
score_counter.place(x=widgets_x_place+390,y=widgets_y_place-35)

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
#_____________________________________________________________
#0000-PICK A NEW CARD Button
####-------------------------Button Text Labels
correct_b__label = customtkinter.CTkLabel(root, text=f"Get Another Card", font=("Courier", 14, "bold"), text_color="Black")
correct_b__label.place(x=150+210+buttons_x_displacement,y=400+buttons_y_displacement+100)

####-------------------------BUTTON-ART / IMAGES
new_card_b__normal_state_image = customtkinter.CTkImage(light_image=Image.open("images/cards_norm.png"),size=(150, 100))
new_card_b__hover_in_image = customtkinter.CTkImage(light_image=Image.open("images/cards_hover.png"),size=(150, 100))
new_card_b__clicked_image = customtkinter.CTkImage(light_image=Image.open("images/cards_clicked.png"),size=(150, 100))

####-------------------------BUTTON-MAIN-FUNCTIONS
# def new_card_button_event():
#----------------------------->THE MAIN FUNCTION OF THIS BUTTON ISS GETTING A NEW CARD ->  picking_word()

####-------------------------BUTTON-CONSTRUCTION Widget
new_card_mark_button = customtkinter.CTkButton(root, image=new_card_b__normal_state_image , text="", height=50, width=150,command=picking_word, fg_color="transparent",border_width=0, hover=False)
new_card_mark_button.place(x=150+210+buttons_x_displacement,y=400+buttons_y_displacement)

####-------------------------BUTTON-Aesthetic-functions
#----HOVER
def new_card_b_hover_in(event):
    new_card_mark_button.configure(image=new_card_b__hover_in_image)
def new_card_b_hover_out(event):
    new_card_mark_button.configure(image=new_card_b__normal_state_image)
#bind events:
new_card_mark_button.bind("<Enter>", new_card_b_hover_in)
new_card_mark_button.bind("<Leave>", new_card_b_hover_out)

#----CLICK-STATE
def new_card_b_clicked(event):
    new_card_mark_button.configure(image=new_card_b__clicked_image)
def new_card_b_unclicked(event):
    new_card_mark_button.configure(image=new_card_b__normal_state_image)
#bind events:
new_card_mark_button.bind("<ButtonPress-1>", new_card_b_clicked)
new_card_mark_button.bind("<ButtonRelease-1>", new_card_b_unclicked)





#_____________________________________________________________
#0000-CHECK-MARK Button
####-------------------------Button Text Labels
correct_b__label = customtkinter.CTkLabel(root, text=f"I know this word", font=("Courier", 14, "bold"), text_color="Black")
correct_b__label.place(x=130+buttons_x_displacement,y=400+buttons_y_displacement+100)

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
check_mark_button.place(x=150+buttons_x_displacement,y=400+buttons_y_displacement)

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
####-------------------------Button Text Labels
wrong_b__label = customtkinter.CTkLabel(root, text=f"I don't know this word", font=("Courier", 14, "bold"), text_color="Black")
wrong_b__label.place(x=600-40+buttons_x_displacement,y=400+buttons_y_displacement+100)

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
wrong_button.place(x=600+buttons_x_displacement,y=400+buttons_y_displacement)

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
#0000-Switch-Lang Button
####-------------------------Button Text Labels
switchL_b__label = customtkinter.CTkLabel(root, text=f"Change Language", font=("Courier", 12, "bold"), text_color="Black")
switchL_b__label.place(x=150+655+buttons_x_displacement,y=200+buttons_y_displacement+25)

####-------------------------BUTTON-ART / IMAGES
switchL_b__normal_state_image = customtkinter.CTkImage(light_image=Image.open("images/lang_folder_norm.png"),size=(100, 75))
switchL_b__hover_in_image = customtkinter.CTkImage(light_image=Image.open("images/lang_folder_hover.png"),size=(100, 75))
switchL_b__clicked_image = customtkinter.CTkImage(light_image=Image.open("images/lang_folder_hover.png"),size=(100, 75))
switchL_b__disabled_image = customtkinter.CTkImage(light_image=Image.open("images/lang_folder_disabled.png"),size=(100,75))

####-------------------------BUTTON-MAIN-FUNCTIONS
# def switchL_button_event():
#----------------------------->THE MAIN FUNCTION OF THIS BUTTON ISS GETTING A NEW CARD ->  pick_language()

####-------------------------BUTTON-CONSTRUCTION Widget
switchL_mark_button = customtkinter.CTkButton(root, image=switchL_b__normal_state_image , text="", height=50, width=150,command=pick_language, fg_color="transparent",border_width=0, hover=False)
switchL_mark_button.place(x=150+640+buttons_x_displacement,y=200+buttons_y_displacement-50)

####-------------------------BUTTON-Aesthetic-functions
#----HOVER
def switchL_b_hover_in(event):
    global LP_Window_Is_ON
    if not LP_Window_Is_ON:
        switchL_mark_button.configure(image=switchL_b__hover_in_image)
def switchL_b_hover_out(event):
    global LP_Window_Is_ON
    if not LP_Window_Is_ON:
        switchL_mark_button.configure(image=switchL_b__normal_state_image)
#bind events: ------------------------------------------------------------>AND BOUND TO "LP_Window_State" only allowed when it's FALSE "off"
switchL_mark_button.bind("<Enter>", switchL_b_hover_in)
switchL_mark_button.bind("<Leave>", switchL_b_hover_out)

#----CLICK-STATE
def switchL_b_clicked(event):
    global LP_Window_Is_ON
    if not LP_Window_Is_ON:
        switchL_mark_button.configure(image=switchL_b__clicked_image)
def switchL_b_unclicked(event):
    global LP_Window_Is_ON
    if not LP_Window_Is_ON:
        switchL_mark_button.configure(image=switchL_b__normal_state_image)
#bind events: ------------------------------------------------------------>AND BOUND TO "LP_Window_State" only allowed when it's FALSE "off"
switchL_mark_button.bind("<ButtonPress-1>", switchL_b_clicked)
switchL_mark_button.bind("<ButtonRelease-1>", switchL_b_unclicked)



#_____________________________________________________________Starting the code with:
picking_word()


#==============END
root.mainloop()
