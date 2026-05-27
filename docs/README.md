# Description of Project
This project scraps words from the nonesense word generated Soybomb.com and uses those words to make gibberish sentences that are then text to speech and saved as wav files. 

# Project Files 
- main.py - main file where all the functions are called from 

- storage_handler - used to write and read in files  
    - write_json - write a variable to a json file  
    - readjson - read in a json file
    - read_csv - read in a csv
    - write_csv - write and save a csv
    - read_voices - read in a csv with the names and codes for Eleven Lab voice models 
- download_handler - download contents from websites
    - download - scrap gibberish words from Soybomb.com
    - downloadIEEE - scap and download IEEE sentences 
- word_handler - organize gibberish words by estimated syllables
- text_to_speech - turn the IEEE and Gibberish sentences into tts and save as wav files 





