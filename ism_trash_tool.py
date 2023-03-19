#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import io
from PIL import Image
import numpy as np
import requests
import streamlit as st

st.title("Environmental Waste Detection Through Neural Networks")
st.markdown(
    "### Predict detected waste and littering in an image",
    unsafe_allow_html=True,
)
st.markdown(
    "### Example:",
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)

before = Image.open("Image #1-A.jpg")
col1.header("Input")
col1.image(before, use_column_width=True)

after = Image.open("mock_example.jpg")
col2.header("Prediction Output")
col2.image(after, use_column_width=True)
# with open("Image #1-A.jpg", "rb") as f:
#     with open("mock_example.jpg", "rb") as g:
#         st.image([f.read(), g.read()])

st.text("Upload an image to recieve output")


def main():
    img_file = st.file_uploader("Upload an image", type=["jpg", "png"])
    if img_file is not None:

        with st.spinner("Predicting..."):
            st.success(f"Your file has been uploaded and processed successfully!")


if __name__ == "__main__":
    main()
