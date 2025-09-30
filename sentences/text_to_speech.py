import pyttsx3 
import wave 
import time 
def _text_to_speech(sent, num_sent):
    engine = pyttsx3.init()
    for i in range(num_sent):
        file= f"sentence_{i+1}.wav"
        thissent = sent[i]
        engine.save_to_file(thissent , file)
    engine.runAndWait()
    ...


# // TODO only makes new files if the files dont exist 