from bs4 import BeautifulSoup
import requests

##TYPING to see if i can figure this out 
def download(url, iterations):
# @@TODO Doc string 
    # Creates a empty list for words 
    words = []
    # reloads the webiste iteration number of times to get new words 
    for i in range(iterations):
        # //TODO dont know what this line does 
        page = requests.get(url)
        # //TODO DOnt know atht his does 
        soup = BeautifulSoup(page.text, "html.parser")
        # Finds all the words that are bold
        Gibberish = soup.find_all("b")
        # //TODO DOUBLe check what this does 
        for gibberish in Gibberish:
            if (" " not in gibberish.text) and ("\n" not in gibberish.text):
                words.append(gibberish.text)
    # Returns the dict of words 
    return words 