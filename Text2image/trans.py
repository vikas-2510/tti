# import the module

#from translate import Translator
from googletrans import Translator

def get_translation(text,):
    translator = Translator()
    translated_text = translator.translate(text, dest='en')
    print("translated_text.text==",translated_text.text)
    return translated_text.text
