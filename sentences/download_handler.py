from bs4 import BeautifulSoup
import requests

def download(url, iterations):
    """Create empty dict, scrap website in iterations, save only gibberish words, return words dict"""
    
    words = []# Creates a empty list for words

    # reloads the webiste iteration number of times to get new words
    for i in range(iterations):
        page = requests.get(url) #gets info from webstire 
        # creates a nested object of the website 
        soup = BeautifulSoup(page.text, "html.parser")

        paragraphs = soup.find_all('span') #gets sections of website that are labeled as 'span' 

        #loops through all the words to get just the text and not html info
        for paragraph in paragraphs:
            words.append(paragraph.text) 

    return words #returns a list of words 


def downloadIEEE(site):
    IEEE = []
    page = requests.get(site) #gets info from site 
    
    soup = BeautifulSoup(page.text, "html.parser") #soups the page info 
    HarvardSentences = soup.find_all("li") #finds all words labeled as <li> 
    for sentences in HarvardSentences:
        IEEE.append(sentences.text)

    return IEEE #returns IEEE sentences 
