import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import streamlit as st

st.title('CV2 Demonstration')

file = st.file_uploader("Please choose a file:")

if file is not None:
    path = file.name
    img = cv.imread(path, 0)
    st.image(img, caption='Original')
        
    if st.button("Apply"):
        edges = cv.Canny(img,100,200)
        st.image(edges, caption='Edges')
        img_bytes = edges.tobytes()
        st.download_button(label="Download Final", data=img_bytes, file_name="Final.png", mime="image/png")
    else:
        st.write("Stoopid")
        
        
