

file = open("List.txt")

text = file.read().splitlines()

req_text = [x.lower() for x in text]




def get_names()
    return req_text[0:req_text.index('')]

def get_word():
    return req_text[len(req_text)-1]


