

file = open("List.txt")


text = file.read().splitlines()

###The site uses small letters only. So we will be converting the user input to small letters.
req_text = [x.lower() for x in text]





### eg:- If the text file is say:-  Adele
###                                 Eminem
###
###                                 Fuck
###
### then the req_text will be a list ['adele','eminem','','fuck']





def get_names():
    return req_text[0:req_text.index('')]

def get_word():
    return req_text[len(req_text)-1]


