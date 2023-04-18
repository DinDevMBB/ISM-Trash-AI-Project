#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import os
import io
import base64
from PIL import Image
from base64 import decodebytes
from io import BytesIO
import numpy as np
import requests
import streamlit as st
from streamlit_image_select import image_select

def create_array():
    directory =  os.path.join(os.getcwd(), "images")
    images = []
    #image_names = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            images.append(os.path.join(directory, filename))
            #image_names.append(filename.split(".")[0])
    return images#, image_names

def main():
    st.set_page_config(layout="wide")
    st.title("Environmental Waste Detection Through Neural Networks")
    url = 'https://raw.githubusercontent.com/1Dragon-Lord1/ISM-Trash-AI-Project/main/image_ex.jpg'
    response = requests.get(url, stream=True)
    image = Image.open(BytesIO(response.content))
    paths = create_array()
    tab1, tab2, tab3 = st.tabs(["Home", "Find your own image", "Help & Contact"])
    with tab1:
        with st.expander("Try some examples"):
            image_path = image_select(
            label="Select an image to test with",
            images = paths,
            #captions= names,
            use_container_width = False
        )
        image = Image.open(image_path)
        img_file = st.sidebar.file_uploader("Upload an image to recieve output", type=["jpg", "png", "jpeg"])
        confidence_threshold = st.sidebar.slider('Confidence threshold: What is the minimum acceptable confidence level for displaying a bounding box?', 0, 100, 50, 1)
        overlap_threshold = st.sidebar.slider('Overlap threshold: What is the maximum amount of overlap permitted between visible bounding boxes?', 0, 100, 50, 1)
        col1, col2 = st.columns(2)
        if img_file is not None:
            image = Image.open(img_file)
            with st.spinner("Uploading..."):
                st.success(f"{img_file.name} has been uploaded and processed successfully!")
            
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

    with tab2:
        st.markdown("Instructions for finding your own image")

    with tab3:
        st.markdown("# Common issues")
        st.markdown("# Contact")
        st.markdown('Let me know if you have any issues with the website you wish to report or anything else you want to communicate with me')

if __name__ == "__main__":
    main()
