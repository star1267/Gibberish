from pathlib import Path
import typer
from typing_extensions import Annotated
from typing import Dict
from .download_handler import download, downloadIEEE
from .word_handler import split_words
from .sentence_handler import build_sentence
from .storage_handler import readjson, write_json, write_csv, read_csv
from .text_to_speech import _IEEE_to_speech, _gibberish_to_speech
from .GTTSPractice import gtts 
import json
import time 


# // TODO I dont know what this line does 
    # I think this is part of inputting values 
app = typer.Typer() 

URL = "https://www.soybomb.com/tricks/words/" #This is the URL for a website that makes gibberish sentences 
HarvardLink = "https://www.cs.columbia.edu/~hgs/audio/harvard.html" #This is a link to the harvard sentences 

#Path is the name of the csv file the sentences are stored in. Num_sent: number of sentences that are generated. 
# one_syllwords: # one syll words, two_syllwords: # two syllable words, words: loads the dict of words 
def _get_sentences(path:Path, num_sent, words_insent, one_syllwords, two_syllwords, words): 
    """Reads to see if there is a file with sentences alread, if goes to sentences builder function"""
    #funtion that reads the csv if it exists
    sent = read_csv(path) 
    # if the sentence list already exists it prints a message saying "Sentence file already exists"
    if sent:
        print("Sentence file already exists")
        return (sent)

    # if the sentence csv file does not exist it moves on to building the sentences 
    else:  
        # goes to the build sentences function and returns the list of sentences 
        sent = build_sentence(num_sent, words_insent, one_syllwords, two_syllwords, words)
        # opens the function to write the csv 
        write_csv(path, sent)
        # If the file didnt exist before NOW it will read the file
        sent = read_csv(path)
        # returns the sentences 
        return(sent)

    
def _get_words(path:Path,num_words:int):
    """This function see's if the list of words exist, if not it scraps the website, stores and organizes the words."""
    # reads in the json word file if it exisits 
    words = readjson(path)
    # If the word file does not already exist it moves to this step 
    if not words:
        print ("wordlist not found ")
        print ("the rest of this needs to be fixed")

        # //TODO  this needs to be fixed because the website was changed so it is not reading any words 
        # creates an empty dic for words 
        words = {}
        # iterations is the number of words requested/50 because there is 50 words on each reloaded soybomb page 
        iterations = int(num_words/50)
        # Function that scraps and downloads words 
        downwords = download(URL, iterations)
        # iterates through each of the words in downwords 
        for tag in downwords:
            # Finds the number of syllables for teh current word
            length = split_words(tag)
            # if the length of the current word is not already a key it makes it a key in the dict words 
            if length not in words:
                words[length] = []
            words[length].append(tag)
        # Sleeps so that the guy whose website it is doesnt kill me 
        time.sleep(1)
        # Writes this dict of words to a json 
        write_json(path, words)
    # returns the dic of words 
    return words
print(_get_words.__doc__)

def IEEEsentences(HarvardLink): 
    json = "./IEEEsentences.json" #Need to add this as an input 
    IEEE = readjson(json)
    if not IEEE: 
        IEEE = downloadIEEE(HarvardLink)
        write_json(json , IEEE)

    return IEEE 


@app.command() #//TODO I dont know what this does but I think it makes it so that the things below can be put in as inputs 

def run(
    # Input number of words to find 
    num_words: Annotated[int, typer.Option(prompt="Number of words to find")] = 100,
    # Input the name of a dict of words 
    dict_path: Annotated[
        str, typer.Option(prompt="Path to the sorted dict")
    ] = r".\wordlist.json",
    # Input the name of a list of sentneces 
    sent_path: Annotated[
        str, typer.Option(prompt="Path to the sorted sentence list")
    ] = r".\gibberishsentences.csv",
    wav_path: Annotated[ 
        str, typer.Option(prompt= "Name of wav files")] = 'sentence', 
    # Input number of sentences to create, Number of words in sentences, number of one syl and number 2 syl. 
    num_sent: Annotated[int, typer.Option(prompt="Number of sentences to make")] = 72,
    words_insent: Annotated[int, typer.Option(prompt="Number of words per sentence")] = 8,
    one_syllwords: Annotated[int, typer.Option(prompt="Number of one syllable words")] = 7,
    two_syllwords: Annotated[int, typer.Option(prompt="Number of two syllable words")] = 1, 
    
) -> None:
    # Makes a dict of words and saves it to a json 
    words = _get_words(Path(dict_path),num_words)
    # Takes that dict of words and uses it to make sentences 
    sent = _get_sentences(Path(sent_path), num_sent, words_insent, one_syllwords, two_syllwords, words) 
    # takes those sentences and text to speech them 
    #tts = _get_tts(sent) 
    #google =gtts (sent)
    IEEE= IEEEsentences(HarvardLink)
    ttsIEEE = _IEEE_to_speech(IEEE) 
    ttsgib = _gibberish_to_speech(sent)

    #Harvard Sentences 
    
    #@@@Todo, make it so that it reads the file if it already exists 

  
# //TODO I dont know what this does but I think it makes it so you can call the inputs 
if __name__ == "__main__":
    app()
# python -m sentences --num-words 10 --dict-path .\words.json --sent-path .\sent.json

