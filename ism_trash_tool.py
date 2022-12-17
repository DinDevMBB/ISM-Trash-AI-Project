#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import io

import numpy as np
import requests
import streamlit as st

st.title("Environmental Waste Detection Through Neural Networks")
st.markdown(
    "### Predict detected waste and littering in an image",
    unsafe_allow_html=True,
)

with open("Image #1-A.jpg", "rb") as f:
    st.image(f.read(), use_column_width=True)

st.text("Upload an image to recieve output")

from PIL import Image


def main():
    img_file = st.file_uploader("Upload an image", type=["jpg", "png"])
    if img_file is not None:

        with st.spinner("Predicting..."):
            st.success(f"Your file has been uploaded and processed successfully!")


if __name__ == "__main__":
    main()

