from urllib2 import urlopen
from bs4 import BeautifulSoup

 ###   a particular artist; the base url is of the form
 ###   "http://www.azlyrics.com/first_letter_of_the_artist_name/artist_name.html"
 ###
 ###    eg:- for adele, its  "http://www.azlyrics.com/a/adele.html"

def get_base_url( artist ):

    first_letter = artist(0)

    return "http://www.azlyrics.com/"+first_letter+"/"+artist+".html"

### In the base-url html file, tags of interest are of the form
###   <a href="../lyrics/adele/daydreamer.html" target="_blank">Daydreamer</a>


def get_song_tags( url, artist ):

    html_text = urlopen( url ).read()

    soup = BeautifulSoup(html_text, "lxml")

    lyrics_tags = soup.select('a[href^="../lyrics/' + str(artist) + '/"]')

    return lyrics_tags


def get_lyrics_link( song_tag ):

    html_link = "http://www.azlyrics.com/"+str(song_tag)[12:str(song_tag).find("target")-2]

    return html_link



def get_occurence( lyric_link, word ):

    htmlfile = urlopen(lyric_link)

    htmltext = htmlfile.read()

    return htmltext.count(str(word))












