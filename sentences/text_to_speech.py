import yaml 
import os
import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

def _IEEE_to_speech(words): 
    ## Load encrypted file 
    with open ('secrets.yaml', 'r') as f: 
        secrets = yaml.safe_load(f)
    apikey = (secrets ['secrets'] ['elevenlabs']['apikey'])

    elevenlabs = ElevenLabs(
        api_key= apikey,
    )

    ##/TODO Make this a for loop so that each entry in IEEE gets looped through and saved 
    response = elevenlabs.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice
        output_format="mp3_22050_32",
        text= words[2], 
        #text = "hello world", 
        model_id="eleven_turbo_v2_5", # use the turbo model for low latency
        # Optional voice settings that allow you to customize the output
        voice_settings=VoiceSettings(
            stability=0.1,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
            speed=1.0,
        ),
    )
 #/ TODO make the wav file name unique 
    save_file_path = f"practice.wav"
    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)
    print(f"{save_file_path}: A new audio file was saved successfully!")
    # Return the path of the saved audio file
    return save_file_path
    ... 