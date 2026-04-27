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
        # creates a nested object of the website 
        soup = BeautifulSoup(page.text, "html.parser")

        paragraphs = soup.find_all('span')
        for i in range (len(paragraphs)):
            print(paragraphs[i].text)
            words.append(paragraphs[i].text) 


    return words


def downloadIEEE(site):
    IEEE = []
    page = requests.get(site)
    # //TODO DOnt know what this does but I think it takes just the text from the webiste
    soup = BeautifulSoup(page.text, "html.parser")
    # Finds all the words that are bold
    HarvardSentences = soup.find_all("li")
    for sentences in HarvardSentences:
        IEEE.append(sentences.text)

    return IEEE
