#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import io
import base64
from PIL import Image
from base64 import decodebytes
from io import BytesIO
import numpy as np
import requests
import streamlit as st

st.title("Environmental Waste Detection Through Neural Networks")
    
def main():
    img_file = st.sidebar.file_uploader("Upload an image to recieve output", type=["jpg", "png", "jpeg"])
    st.sidebar.write('Find additional images to test with here')
    confidence_threshold = st.sidebar.slider('Confidence threshold: What is the minimum acceptable confidence level for displaying a bounding box?', 0, 100, 50, 1)
    overlap_threshold = st.sidebar.slider('Overlap threshold: What is the maximum amount of overlap permitted between visible bounding boxes?', 0, 100, 50, 1)
    col1, col2 = st.columns(2)
    if img_file is not None:
        with st.spinner("Uploading..."):
            st.success(f"Your file has been uploaded and processed successfully!")
        image = Image.open(img_file)
    else:
        url = 'https://raw.githubusercontent.com/1Dragon-Lord1/ISM-Trash-AI-Project/main/image_ex.jpg'
        response = requests.get(url, stream=True)
        image = Image.open(BytesIO(response.content))
    col1.caption("Input")
    col1.image(image, use_column_width=True)
    buffered = io.BytesIO()
    image.save(buffered, quality = 90, format = 'JPEG')
    img_str = base64.b64encode(buffered.getvalue())
    upload_url = ''.join(['https://detect.roboflow.com//waste-detection-vnfx1/2?api_key=', 
                         st.secrets["api_key"],
                         '&format=image',
                         f'&overlap={overlap_threshold}',
                         f'&confidence={confidence_threshold}',
                         '&stroke=6',
                         '&labels=False'])
    r = requests.post(upload_url, data = img_str, headers = {'Content-Type': 'application/x-www-form-urlencoded'})
    image = Image.open(BytesIO(r.content))
    buffered = io.BytesIO()
    image.save(buffered, quality=90, format='JPEG')
    col2.caption("Prediction Output")
    col2.image(image, use_column_width=True)
    #upload_url = ''.join(['https://detect.roboflow.com//waste-detection-vnfx1/2?api_key=', 
                         #st.secrets["api_key"]])
    #r = requests.post(upload_url, data = img_str, headers = {'Content-Type': 'application/x-www-form-urlencoded'})
    #output_dict = r.json();
    #confidences = [box['confidence'] for box in output_dict['predictions']]

if __name__ == "__main__":
    main()
