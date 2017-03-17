###WnCC_Web_Scraping###

In a file named Input.txt, you have a list of n artists followed by a blank line, followed by a word x.
Sort a list of n artists based on their frequency of usage of a word x.


Approach - We will be scraping " https://www.azlyrics.com"  to get hold of the lyrics.

                 * Get the artist names and the word from the List.txt file

                 * Go to the BASE PAGE that contains links for lyrics of all the songs of the artist.
                    
                    It contains exhaustive links to pages that have lyrics.
                    eg:- for artist Adele, it  "http://www.azlyrics.com/a/adele.html"
                   
                   Parse the page for appropriate html tags, that will provide us the individual url address
                   of the page that contains lyrics to a particular song
                   
                   eg of a tag:-"<a href="../lyrics/adele/daydreamer.html" target="_blank">Daydreamer</a>"
                   
                   eg of url derived from the tag:-  "http://www.azlyrics.com/lyrics/adele/daydreamer.html"
                 
                 * Traverse through each of the links. Get hold of the html file of that page and search for
                   our word and record it number of occurrences
                   
We will be using the python module BeautifulSoup for scraping purposes

Plans to implement multithreading soon. 

###IMPORTANT###

It's important to attest some some sort of control mechanism so that you dont send a large number of requests.You may be blocked by the site, if it happens so. This can be done by tweaking with the url_functions.py by adding wait() command.

As of now, I havent added it yet. 

Also, there is a 'check' variable in main.py. It controls the number of songs that we search the word for a particular artist.
I've currently put the limit to 5. But one can remove it as a whhole, if onewants to search all the songs.

       
      
