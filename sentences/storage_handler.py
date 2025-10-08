from pathlib import Path 
from typing import Dict
import json 
import os.path 
import csv 

#creates an empty dict to store the words in the word file 
filecontent = {}
def readjson(path:Path):
    """This function checks to see if there is already a json file under the name. If so it reads the file and returns the content of the file."""

    # Checks if the json file exists. If not it returns nothing and the function is done 
    if not os.path.exists(path): 
        return None 

    #  if the json file does exist it moves on to this 
    else:
        # Opens the json file and reads the content 
        with open(path, 'r') as input: 
            # Puts the content from the json in the dict filecontent 
            filecontent = json.load(input)  
            # returns the filecontent 
            return filecontent
    ...

def write_json(path:Path,content:Dict):
    """This creates a json file and write the dict to that file."""
    #
    with open(path, 'w') as output:
        json.dump (content, output, indent =2)

    ...

def read_csv(path:Path):
    """This checks if there is a csv file with sentences. if there is already a file it reads the file and returns content """

    # Creates a list for just the clean sentences 
    cleansent = []
    # If the file does exist it returns nothing 
    if not os.path.exists(path): 
        return None 
    # If the file does exist it moves on to this part 
    else:
        # Opens the file and reads it 
        with open(path, 'r') as csv_file: 
            # creates a list of the file content 
            csv_reader = csv.reader(csv_file)
            # iterates through each line in the file 
            for line in csv_reader: 
                # Creates a new list of just the last column in the file which is the clean sentences 
                cleansent.append(line[2])
    # returns the clean sentences 
    return (cleansent)



def write_csv(path, sentences): 
    """This creates a csv and then write the sentences to that csv"""
    # Opens the csv file to write to it 
    with open(path, 'w', newline='') as f: 
        # //TODO I dont know what this does 
        writer = csv.writer(f)
        # //TODO I DONT KNOW WHAT this does 
        writer.writerows(sentences) 
    ...