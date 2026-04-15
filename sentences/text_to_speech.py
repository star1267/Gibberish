import yaml 
import os
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from datetime import datetime
from .storage_handler import read_voices
from pathlib import Path

def texttospeech(Stim, voice_path, stimtype): 
    """ This function is used to Text to speech the stimuli"""
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
    parent_folder = "WavStorage" #parent folder to our stimulit 
    subfolderTime = f'{current_time}' #unique file name
    subfolder = "April062026" #Name of folder stim are stored in 
    foldername = os.path.join(parent_folder, subfolder) #checks if folder exists 
    os.makedirs(foldername, exist_ok=True)  # actually creates it

    stab = 1 # set stability setting
    lenvoices = len(voices) #get number of voices

    for v in range(lenvoices): 
        voice = voices[v] #iterates through voices
        name = names [v] #iterates through names
        for i in range (len(Stim)): #Loops through each sentence 
            response = elevenlabs.text_to_speech.convert( ##creates a variable response with contains the audio, calls 11labs function
                voice_id= voice,  #Sets voice for this loop
                output_format="wav_44100", #file type
                text= Stim[i], #sets stimulit that will be tts
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
            filename = f"{"Newsenteces"}{stimtype}{name}{i+1}.wav"
            save_file_path = os.path.join(foldername, filename) #Makes file save to the new folder '

            # Writing the audio to a file
            with open(save_file_path, "wb") as f:
                for chunk in response:
                    if chunk:
                        f.write(chunk)
        ...
    ...
