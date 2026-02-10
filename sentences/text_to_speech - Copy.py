import pyttsx3 
import wave 
import time 
import os 
from datetime import datetime
from pathlib import Path 

#//TODO Change this so that it is saving with todays date and to a new folder 
    #and probably dont need to check if it exists then 

def _text_to_speech(sent, num_sent, wav_path):
    """Takes the sentences, tts them and save as wav files"""
    current_time = datetime.now().strftime("%Y-%m-%d")
    script_dir = Path(__file__).parent #Path of parent directory for this script
    path = script_dir / f'Gibberish_Wav_{current_time}' #path to folder 
    path.mkdir(parents = True, exist_ok =True)



    engine = pyttsx3.init()
    for i in range(num_sent): 
        #Creates a file name that is INPUT+iteration number 
        file= f'Gibberish_{current_time}_{i+1}.wav'
        thissent = sent[i]
            #saves sentences as wav file
        engine.save_to_file(thissent,file)
    #files dont save until this line 
    engine.runAndWait()
    ...




# @@TODO change the folder it saves to 
def _IEEE_to_speech(IEEE): 
    """Checks to see if IEEE wav files exist. If they do it ends. If not it makes the wav files"""
    ## sets file check to true so it will only print message one first iteration 
    filecheck = True
    engine = pyttsx3.init()
    for i in range(720):
        #creates file name with iteration number
        file= f'{'HarvardSentence'}_{i+1}.wav'
        #Checks if that file already exists 
        if os.path.exists(file):
            #if it exists and its the first iteratino it prints the message 
            if filecheck: 
                print ("IEEE wav file already exists, change file name")
            #turns off message 
            filecheck = False
        # if the file doesnt exist it makes the file 
        else: 
            thissent = IEEE[i]
            #saves sentences as wav file
            engine.save_to_file(thissent, file)
    #files dont save until this line 
    engine.runAndWait()

    ...




#@///TODO save Harvard sentences into a json 