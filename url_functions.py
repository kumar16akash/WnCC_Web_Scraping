import urllib2
from bs4 import BeautifulSoup

def get_base_url( artist ):

    first_letter = artist(0)

    return "http://www.azlyrics.com/"+first_letter+"/"+artist+".html"


def get_song_tags( artist ):

    html_text = urllib2.urlopen(get_base_url( artist )).read()

    soup = BeautifulSoup(html_text, "lxml")

    lyrics_tags = soup.select('a[href^="../lyrics/' + str() + '/"]')

    return lyrics_tags



def get_lyrics_link( song_tag ):

    html_link = "http://www.azlyrics.com/"+str(song_tag)[12:str(song_tag).find("target")-2]

    return html_link



def get_number( lyric_link, word ):

    htmlfile = urllib2.urlopen(lyric_link)

    htmltext = htmlfile.read()

    return  htmltext.count(str(word))












