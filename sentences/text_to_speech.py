import yaml 
import os
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from datetime import datetime
from .storage_handler import read_voices
from pathlib import Path

def texttospeech(Stim, voice_path, stimtype): 
    #Create list of voices and names by reading csv
    voices , names = read_voices(Path(voice_path))

    ## Load encrypted file 
    with open ('secrets.yaml', 'r') as f:  #opens yaml with apikey
        secrets = yaml.safe_load(f)
    apikey = (secrets ['secrets'] ['elevenlabs']['apikey']) #read and store API key
    elevenlabs = ElevenLabs( #tells 11labs what the api key is 
        api_key= apikey,
    )
    current_time = datetime.now().strftime("%Y-%m-%d-%I-%M-%S") #calculates current time 

    parent_folder = "WavStorage"
    subfolderTime = f'{current_time}' #unique file name
    subfolder = "StimuliSamples"
    foldername = os.path.join(parent_folder, subfolder)
    os.makedirs(foldername, exist_ok=True)  # actually creates it

    stab = 0.0
    length = len(voices)
    for v in range(length): 
        voice = voices[v]
        name = names [v]
        for i in range (1): #Loops through each sentence 
            response = elevenlabs.text_to_speech.convert( ##creates a variable response with contains the audio, calls 11labs function
                voice_id= voice,  
                output_format="mp3_44100_128", 
                text= Stim[i], 
                model_id="eleven_turbo_v2_5", # use the turbo model for low latency
                # Optional voice settings that allow you to customize the output
                voice_settings=VoiceSettings(
                    stability= stab, #(lower = more expressive, higher = less expressive) 0-1 
                    similarity_boost=1.0, #Lower = less like original voice; higher = more accurate to voice
                    style=0.0, #Lower = neutral; higher = more stylized or dramatic
                    use_speaker_boost=True, #Turns the speaker boost on/off; helps with projection and clarity
                    speed=0.8, #1.0 = normal speed; below 1 = slower; above 1 = faster
                ),
            )
            
            #filename = f'{stimtype}{current_time}_{i+1}.mp3' #Unique file name with current time
            filename = f"{stimtype}{name}{stab}.mp3"
            save_file_path = os.path.join(foldername, filename) #Makes file save to the new folder '

            # Writing the audio to a file
            with open(save_file_path, "wb") as f:
                for chunk in response:
                    if chunk:
                        f.write(chunk)
            print(f"{save_file_path}: A new audio file was saved successfully!")
            # Return the path of the saved audio file
        ...
    ...
