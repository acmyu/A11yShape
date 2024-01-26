# https://stackoverflow.com/questions/77284901/upload-an-image-to-chat-gpt-using-the-api

import base64
import requests
from dotenv import load_dotenv
import os
from io import BytesIO
from PIL import Image
import json

from os import listdir
from os.path import isfile, join

load_dotenv()

# OpenAI API Key
api_key = os.getenv("OPENAI_KEY")


models_folder = 'models'
views_folder = 'temp'

file = 'Bacteriophage.scad'

print(file)
fp = join(models_folder, file)
outpath = join(views_folder, file.rsplit('.', 1)[0])
if not os.path.exists(outpath):
    os.makedirs(outpath)
    
x=0
y=0
z=1
outfile = join(outpath, str(x+1)+str(y+1)+str(z+1)+'.png')

cmd = 'openscad -o '+outfile+' --camera '+str(x)+','+str(y)+','+str(z)+',0,0,0 --viewall --autocenter --imgsize=2048,2048 '+fp
#print(cmd)
os.system(cmd)



# Function to encode the image
def encode_image(image_path):
    img = Image.open(image_path)
    newsize = (256, 256)
    img = img.resize(newsize)
    im_file = BytesIO()
    img.save(im_file, format="JPEG")
    im_bytes = im_file.getvalue()  # im_bytes: image in binary format.
    return base64.b64encode(im_bytes).decode('utf-8')


# Path to your image
image_path = "temp/Bacteriophage/"+str(x+1)+str(y+1)+str(z+1)+'.png'

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Describe the shape of this dinosaur-headed robot in detail"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
response = response.json()

print(response['choices'][0]['message']['content'])
