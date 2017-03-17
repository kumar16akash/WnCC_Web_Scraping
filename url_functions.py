from urllib2 import urlopen
from bs4 import BeautifulSoup

 ###   a particular artist; the base url is of the form
 ###   "http://www.azlyrics.com/first_letter_of_the_artist_name/artist_name.html"
 ###
 ###    eg:- for adele, its  "http://www.azlyrics.com/a/adele.html"

def get_base_url( str ):

    first_letter = str[0]

    return "http://www.azlyrics.com/"+first_letter+"/"+str+".html"

### In the base-url html file, tags of interest are of the form
###   <a href="../lyrics/adele/daydreamer.html" target="_blank">Daydreamer</a>


def get_song_tags( url, artist ):

    html_text = urlopen( url ).read()

    soup = BeautifulSoup(html_text, "lxml")
    ### We need only the a tags that have href = ../lyrics/artist_name/song_name.
    ### The below soup.select helps in parsing. It only accepts tags that are beginning with
    ### ../lyrics/(artist_name)/
    lyrics_tags = soup.select('a[href^="../lyrics/' + str(artist) + '/"]')

    return lyrics_tags

### Get the link from the song tag
def get_lyrics_link( song_tag ):


    ### eg: - for the tag - "<a href="../lyrics/adele/daydreamer.html" target="_blank">Daydreamer</a>"
    ### the link will be :-"http://www.azlyrics.com/lyrics/adele/daydreamer.html"

    html_link = "http://www.azlyrics.com/"+str(song_tag)[12:str(song_tag).find("target")-2]

    return html_link


###Go through the html file of the link, and count the occurrences of the word
def get_occurence( lyric_link, word ):

    htmlfile = urlopen(lyric_link)

    htmltext = htmlfile.read()

    return htmltext.count(str(word))












