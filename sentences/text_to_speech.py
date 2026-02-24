import yaml 
import os
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from datetime import datetime
from pathlib import Path 

#import time 
#import uuid

def _IEEE_to_speech(IEEE): 
    ## Load encrypted file 
    with open ('secrets.yaml', 'r') as f:  #opens yaml with apikey
        secrets = yaml.safe_load(f)
    apikey = (secrets ['secrets'] ['elevenlabs']['apikey']) #read and store API key

    elevenlabs = ElevenLabs( #tells 11labs what the api key is 
        api_key= apikey,
    )
    current_time = datetime.now().strftime("%Y-%m-%d-%I-%M-%S") #calculates current time 
    foldername = f'IEEE{current_time}' #unique file name
    os.mkdir (foldername) #unique folder 

    for i in range (len(IEEE)): #Loops through each sentence 
        response = elevenlabs.text_to_speech.convert( ##creates a variable response with contains the audio, calls 11labs function
            voice_id="pNInz6obpgDQGcFmaJgB", # sets voice to "Adam"
            output_format="wav", 
            text= IEEE[i], 
            model_id="eleven_turbo_v2_5", # use the turbo model for low latency
            # Optional voice settings that allow you to customize the output
            voice_settings=VoiceSettings(
                stability=0.1, #(lower = more expressive, higher = less expressive) 0-1 
                similarity_boost=1.0, #Lower = less like original voice; higher = more accurate to voice
                style=0.0, #Lower = neutral; higher = more stylized or dramatic
                use_speaker_boost=True, #Turns the speaker boost on/off; helps with projection and clarity
                speed=1.0, #1.0 = normal speed; below 1 = slower; above 1 = faster
            ),
        )
        
        #filename = f'IEEE_{current_time}_{i+1}.wav' #Unique file name with current time
        filename = f'IEEE{i+1}.wav'
        save_file_path = os.path.join(foldername, filename) #Makes file save to the new folder 
        # Writing the audio to a file
        with open(save_file_path, "wb") as f:
            for chunk in response:
                if chunk:
                    f.write(chunk)
        print(f"{save_file_path}: A new audio file was saved successfully!")
        # Return the path of the saved audio file
    return save_file_path
    ... 


def _gibberish_to_speech(Gibberish): 
    ## Load encrypted file 
    with open ('secrets.yaml', 'r') as f:  #opens yaml with apikey
        secrets = yaml.safe_load(f)
    apikey = (secrets ['secrets'] ['elevenlabs']['apikey']) #read and store API key

    elevenlabs = ElevenLabs( #tells 11labs what the api key is 
        api_key= apikey,
    )
    current_time = datetime.now().strftime("%Y-%m-%d-%I-%M-%S") #calculates current time 
    foldername = f'Gibberish{current_time}' #unique file name
    os.mkdir (foldername) #unique folder 

    for i in range (len(Gibberish)): #Loops through each sentence 
        response = elevenlabs.text_to_speech.convert( ##creates a variable response with contains the audio, calls 11labs function
            voice_id="pNInz6obpgDQGcFmaJgB", # sets voice to "Adam"
            output_format="wav", 
            text= Gibberish[i], 
            model_id="eleven_turbo_v2_5", # use the turbo model for low latency
            # Optional voice settings that allow you to customize the output
            voice_settings=VoiceSettings(
                stability=0.1, #(lower = more expressive, higher = less expressive) 0-1 
                similarity_boost=1.0, #Lower = less like original voice; higher = more accurate to voice
                style=0.0, #Lower = neutral; higher = more stylized or dramatic
                use_speaker_boost=True, #Turns the speaker boost on/off; helps with projection and clarity
                speed=1.0, #1.0 = normal speed; below 1 = slower; above 1 = faster
            ),
        )
        
        #filename = f'IEEE_{current_time}_{i+1}.wav' #Unique file name with current time
        filename = f'Gibberish{i+1}.wav'
        save_file_path = os.path.join(foldername, filename) #Makes file save to the new folder 
        # Writing the audio to a file
        with open(save_file_path, "wb") as f:
            for chunk in response:
                if chunk:
                    f.write(chunk)
        print(f"{save_file_path}: A new audio file was saved successfully!")
        # Return the path of the saved audio file
    return save_file_path
    ... 

