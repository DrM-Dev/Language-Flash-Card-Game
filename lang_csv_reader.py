#_______________Imports:
import pandas
from gevent.util import print_run_info
#
import random

#========================Data-Base SETUP
chosen_lang_DF = pandas.read_csv(r"data/french_words.csv")
# print(nato_phonetics_DF)

#====================================================================================DB to DIC
#Turning Database into Dictionary:
chosen_lang_DIC = { row_info.French:row_info.English for (index,row_info) in chosen_lang_DF.iterrows()}

#====================================================================================DIC to DS (Data Series) "to pick keys ONLY"
# TARGETED DIC => chosen_lang_DIC
lang_series = pandas.Series(chosen_lang_DIC)
lang_keys_list = [ keys[0] for keys in lang_series.items() ]
####DEBUG
# print(lang_keys_list)

#===================================================================================== PICKING A RANDOM KEY [Word & it's meaning]
##############################
def pick_random_word(exception_list):
    global chosen_lang_DIC
    global lang_keys_list
    #======
    resalt_tuple = ""
    random_key = random.choice(lang_keys_list)
    #######
    if random_key not in exception_list:
        #
        picked_word = random_key
        picked_meaning = chosen_lang_DIC[picked_word]
        #
        print(f"this is the word= {picked_word}\nthis is the meaning= {picked_meaning}")
        # return something
        ############
        resalt_tuple = (picked_word,picked_meaning)
        ############
    else:
        pick_random_word(exception_list)

    #___________________________________
    #=====EMPTY TUPLE BUG FIX:
    if resalt_tuple != "" or resalt_tuple != None:
        return resalt_tuple
    else:
        pick_random_word(exception_list)
