# Imports the Google Cloud client library

import os    
from google.cloud import translate_v2 as translate

credential_path = "C:\TranslationAPI\TranslationAPI-a9270b8d6c1f.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# Instantiates a client
translate_client = translate.Client()

# The text to translate
text = 'Bonjour!'
# The target language
target = 'vi'



# Translates some text into Vietnamese
translation = translate_client.translate(
    text,
    target_language=target)

print('Text: {}'.format(text))
print('Translation: {}'.format(translation['translatedText']))