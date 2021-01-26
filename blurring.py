# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 18:32:32 2021

@author: bqure
"""


import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
# To install this module, run:
# python -m pip install Pillow
from PIL import Image, ImageDraw,ImageFilter
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person

KEY = "add your key here"
ENDPOINT = "https://sydney123.cognitiveservices.azure.com/"

# Create face client azure object from .
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))


# Detect a face in an image that contains a single face
single_face_image_url = "https://media-exp1.licdn.com/dms/image/C4E03AQGEgXxIOj1RNw/profile-displayphoto-shrink_800_800/0/1604764065385?e=1617235200&v=beta&t=U62KpD7QjE7RfZ-JB6gG3cFOkKoyIBTcMzsb9LSdERg"
single_image_name = os.path.basename(single_face_image_url)
# We use detection model 3 to get better performance.
detected_faces = face_client.face.detect_with_url(url=single_face_image_url, detection_model='detection_03')
if not detected_faces:
    raise Exception('No face detected from image {}'.format(single_image_name))

# Display the detected face ID in the first single-face image.
# Face IDs are used for comparison to faces (their IDs) detected in other images.
print('Detected face ID from', single_image_name, ':')
for face in detected_faces: print (face.face_id)
print()

# Save this ID for use in Find Similar
first_image_face_ID = detected_faces[0].face_id
def getRectangle(faceDictionary):
    rect = faceDictionary.face_rectangle
    left = rect.left
    top = rect.top
    right = left + rect.width
    bottom = top + rect.height
    listbb.append(rect.width)
    listbb.append(rect.height)
    return ((left, top), (right, bottom))
# Detect a face in an image that contains a single face
urlo=["https://media-exp1.licdn.com/dms/image/C4E03AQGEgXxIOj1RNw/profile-displayphoto-shrink_800_800/0/1604764065385?e=1617235200&v=beta&t=U62KpD7QjE7RfZ-JB6gG3cFOkKoyIBTcMzsb9LSdERg","https://media-exp1.licdn.com/dms/image/C5603AQH65OSX923CVQ/profile-displayphoto-shrink_800_800/0/1588008960533?e=1617235200&v=beta&t=odGh-5dWKgqUBdm2M21O-pK3R-hnzL19V0eoGcXmQSY","https://media-exp1.licdn.com/dms/image/C5603AQHv9IK9Ts0dFA/profile-displayphoto-shrink_800_800/0/1517497547164?e=1617235200&v=beta&t=rjlXWcuZOZOXp1mZXnPYKchV5WZT8d9WjwIkpOi2YI0"]
for x in range(0,len(urlo)):

    single_image_name = os.path.basename(urlo[x])
    # We use detection model 3 to get better performance.
    detected_faces = face_client.face.detect_with_url(url=urlo[x], detection_model='detection_03')
    if not detected_faces:
        raise Exception('No face detected from image {}'.format(single_image_name))

    # Convert width height to a point in a rectangle
    listbb=[]
    # downloading image from url
    response = requests.get(urlo[x])
    img = Image.open(BytesIO(response.content))
    mask = Image.new('L',img.size)
    sizeofimage=img.size
    # make red box
    print('Drawing rectangle around face... see popup for results.')
    draw = ImageDraw.Draw(mask)

    for face in detected_faces:
        draw.rectangle(getRectangle(face), outline='red',fill=255)
   
    imgblur = img.filter(ImageFilter.GaussianBlur(radius=5))

    masked_image = Image.composite(img,imgblur,mask)
    masked_image.show()
    # calculate the percentage of face with whole photo
    percentage=((listbb[0]*listbb[1])/(sizeofimage[0]*sizeofimage[1]))*100
    print("percentage of face of face with whole photo of photo "+str(x))
    print(percentage)
    if(percentage<50):
        print("face size is small")
    else:
        print("face size is fit")
