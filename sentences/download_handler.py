from bs4 import BeautifulSoup
import requests

##TYPING to see if i can figure this out 
def download(url, iterations):
    """Create empty dict, scrap website in iterations, save only gibberish words, return words dict"""
    # Creates a empty list for words 
    words = []
    # reloads the webiste iteration number of times to get new words 
    for i in range(iterations):
        # //TODO dont know what this line does but I think it stores the webiste infromation 
        page = requests.get(url)
        # //TODO DOnt know what this does but I think it takes just the text from the webiste 
        soup = BeautifulSoup(page.text, "html.parser")
        # Finds all the words that are bold
        Gibberish = soup.find_all("b")
        # for each word in Gibberish, it stores the ones that dont have "" and \n
        for gibberish in Gibberish:
            if (" " not in gibberish.text) and ("\n" not in gibberish.text):
                words.append(gibberish.text)
    # Returns the dict of words 
    return words 