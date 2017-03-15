''' ##################################################################################################
    Alok Kumar Bishoyi
    160040093, Civil

    Objective - Given a list of artist names, we would like to find out the number of of
                occurrences of the word in their lyrics.

                We would be reading the list and the word to be searched from "List.txt" file

    Approach - We will be scraping " https://www.azlyrics.com"  to get hold of the lyrics.

                 * Get the artist names and the word from the List.txt file

                 * Go to the BASE PAGE that contains links for lyrics of all the songs of the artist.
                   Parse the page for appropriate html tags, that will provide us the individual url address
                   of the page that contains lyrics to a particular song
                 * Traverse through each of the links. Get hold of the html file of that page and search for
                   our word and record it number of occurrences
    #####################################################################################################
    '''

###Contains functions to access text file and operate on it
import text_file

###Contains functions for scraping and crawling
import url_functions

###For sorting the dictionary where we will be keeping the record of artist names and the word-occurrence
from operator import itemgetter


###get list of artist names
names = text_file.get_names()

###get the word
word = text_file.get_word()

###initiate the dictionary where we will keep track of artist names and the word occurence
record = []


for name in names:
    '''
        get base_url. It contains exhaustive links to pages that have lyrics.
        eg:- for artist Adele, it  "http://www.azlyrics.com/a/adele.html"
    '''
    base_url = url_functions.get_base_url( name )

    '''
        Get the appropriate tags in the html file that will help us get url address of the lyric pages
        eg:- "<a href="../lyrics/adele/daydreamer.html" target="_blank">Daydreamer</a>"
             will help us get the url address of the page that contains lyrics to the song
             "daydreamer" of the artist adele

    '''
    tags = url_functions.get_song_tags( base_url )

    ###Create a counter which will track the occurrence of the word
    counter = 0


    check = 0
    for tag in tags:


        if check == 3:
            break

        '''
            Get the url address of the site associated with the tag that contains lyrics.
            eg:- "http://www.azlyrics.com/lyrics/adele/daydreamer.html"

        '''
        lyric_link = url_functions.get_lyrics_link( tag )

        ###Count the occurrence of the word
        occurence = url_functions.get_occurence( lyric_link )

        ###Update counter
        counter += occurence
        check += 1
    #Update record dictionary with a list that contains the artist name and the occurrence
    record.append({'name': name, 'number': counter})


#Sort the list based on occurence
newlist = sorted(record, key = itemgetter('number'), reverse = True)

#Print the result
for dictionary in newlist:
    print dictionary['name']+" -- number of times profanity used -- "+str(dictionary['number'])





