import pyttsx3 
import wave 
import time 
import os 
def _text_to_speech(sent, num_sent, wav_path):
    """Takes the sentences, tts them and save as wav files"""
    engine = pyttsx3.init()
    for i in range(num_sent):
        file= f'{wav_path}_{i+1}.wav'
        if os.path.exists(file):
            print ("wav file already exists. Rename files")
        else: 
            thissent = sent[i]
            #saves sentences as wav file
            engine.save_to_file(thissent , file)
    #files dont save until this line 
    engine.runAndWait()
    ...


# // TODO only makes new files if the files dont exist 