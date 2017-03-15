import text_file
import url_functions
from operator import itemgetter



names = text_file.get_names()

word = text_file.get_word()


record = []


for name in names:

    base_url = url_functions.get_base_url( name )

    tags = url_functions.get_song_tags( base_url )


    counter = 0


    check = 0
    for tag in tags:


        if check == 3:
            break

        lyric_link = url_functions.get_lyrics_link( tag )


        occurence = url_functions.get_occurence( lyric_link )

        counter+=occurence
        check+=1

    record.append({'name': name, 'number': counter})



newlist = sorted(record, key = itemgetter('number'), reverse = True)

for dictionary in newlist:
    print dictionary['name']+" -- number of times profanity used -- "+str(dictionary['number'])





