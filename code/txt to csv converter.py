#_______________Imports:
import time
import pandas
from gevent.util import print_run_info

#========================FETCH TEXT:
text_data_column = pandas.read_csv("data/French/fr_500.csv")
# print(text_data_frame)
#########################
finalized_list = []
empty_meaning_list = []
n = 0
#########################
for index, row in text_data_column.head(500).iterrows(): #<----------we will take 1k from each lang for this simple game project :)
    character = row.to_string(index=False)
    character_string = str(character)
    #
    filter0 = character_string.replace("0","")
    filter1 = filter0.replace("1", "")
    filter2 = filter1.replace("2", "")
    filter3 = filter2.replace("3", "")
    filter4 = filter3.replace("4", "")
    filter5 = filter4.replace("5", "")
    filter6 = filter5.replace("6", "")
    filter7 = filter6.replace("7", "")
    filter8 = filter7.replace("8", "")
    filter9 = filter8.replace("9", "")
    #
    finalized_list.append(filter9)
    empty_meaning_list.append("")
    #
    n +=1
    print(f"+{n} ----> {filter9}")
##########################
print(finalized_list)

#======================================================
time.sleep(1)
#========================TURNING EXTRACTED LIST TO DIC:
# 1. Create a sample DataFrame
data_dic = {
    'Spanish': finalized_list,
    'English': empty_meaning_list #<----------------Using Google-Sheets for translation
}

#========================TURNING DIC TO DATA-FRAME:
data_frame = pandas.DataFrame(data_dic)

# 2. Save to CSV
data_frame.to_csv('sp_500.csv', index=False)
