import pyttsx3 
import wave 
import time 
import os 
def _text_to_speech(sent, num_sent, wav_path):
    """Takes the sentences, tts them and save as wav files"""
    # sets file check to true so it will only print message one first iteration 
    filecheck = True
    engine = pyttsx3.init()
    for i in range(num_sent):
        #Creates a file name that is INPUT+iteration number 
        file= f'{wav_path}_{i+1}.wav'
        #Checks if that file exsits 
        if os.path.exists(file):
            #If the file exists AND its the first iteration it displays this message
            if filecheck: 
                print ("wav file already exists. Rename files")
            filecheck = False
        else: 
            thissent = sent[i]
            #saves sentences as wav file
            engine.save_to_file(thissent , file)
    #files dont save until this line 
    engine.runAndWait()
    ...


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
            filecheck = False4
        # if the file doesnt exist it makes the file 
        else: 
            thissent = IEEE[i]
            #saves sentences as wav file
            engine.save_to_file(thissent, file)
    #files dont save until this line 
    engine.runAndWait()


    ...




#@///TODO save Harvard sentences into a json 