import requests
import io
from PIL import Image
from googletrans import Translator
#from pathlib import Path

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}
def process(intext):
	
	#translatedtext=get_translation(intext,ln)
	def query(payload):
		response = requests.post(API_URL, headers=headers, json=payload)
		return response.content
	image_bytes = query({"inputs": str(intext),})
	image = Image.open(io.BytesIO(image_bytes))
	image.show()
	intext=intext.split()
	image = image.save(str(intext[0])+"_.jpg") 
#translation = get_translation()
#process("ಕೆಂಪು ಟೀ ಶರ್ಟ್ ಧರಿಸಿದ ಹುಡುಗ","en")
