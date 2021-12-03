#Library imports
import numpy as np
import streamlit as st
import cv2
from PIL import Image
import pytesseract



#Setting Title of App
st.title("Text extracting image")
st.markdown("Upload an image with text on it")

#Uploading the dog image
imageText = st.file_uploader("Choose an image...")
submit = st.button('Extract')

#On predict button click
if submit:


    if imageText is not None:

        # Convert the file to an opencv image.
        file_bytes = np.asarray(bytearray(imageText.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        # Displaying the image
        st.image(opencv_image, channels="BGR")
        # Converting image into gray scale
        gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
        #Converting image back to rbg
        imageT = Image.fromarray(gray)
        # Extracting text from image
        custom_config = r'-l eng --oem 3 --psm 6'
        text = pytesseract.image_to_string(imageT, config= custom_config)
        #remove symbol 
        characters_to_remove = "!()@—*“>+-/,'|£#%$&^_~"
        new_string =text
        for c in characters_to_remove:
            new_string = new_string.replace(c,"")
        #Converting string into list of display
        #new_string = new_string.split("\n")
        st.write(new_string)
