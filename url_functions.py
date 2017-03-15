import urllib2
from bs4 import BeautifulSoup

def get_base_url( str ):
    first_letter = str(0)
    return "http://www.azlyrics.com/"+first_letter+"/"+str+".html"


def get_lyrics_tags( str ):

    html_text = urllib2.urlopen(url).read()

    soup = BeautifulSoup(html_text, "lxml")













