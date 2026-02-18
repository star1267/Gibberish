import os 
import signal 
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
import yaml 

def _IEEE_to_speech(IEEE,): 
    ## Load encrypted file 
    with open ('secrets.yaml', 'r') as f: 
        secrets = yaml.safe_load(f)
    apikey = (secrets ['secrets'] ['elevenlabs']['apikey'])

    #decrypt file so that i have the API as a variable 
    ##USE Youtube video to tts the sentences 
    

    ... 