import streamlit as st
import numpy as np
import cv2
from  PIL import Image, ImageEnhance 

st.title(":heart_eyes:")

col1, col2 = st.columns( [0.8, 0.2])
with col1:               
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Upload your photo here...</p>', unsafe_allow_html=True)
    
st.sidebar.markdown('<p class="font">My First Photo Converter App</p>', unsafe_allow_html=True)
with st.sidebar.expander("About the App"):
     st.write("""
        Use this simple app to convert your favorite photo to a pencil sketch, a grayscale image or an image with blurring effect. \n. Hope you enjoy!
     """) 
uploaded_file = st.camera_input("") 

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns( [0.5, 0.5])
    with col1:
        st.markdown('<p style="text-align: center;">Before</p>',unsafe_allow_html=True)
        st.image(image,width=300)  

          
if uploaded_file is not None:
    with col2:
            st.markdown('<p style="text-align: center;">After</p>',unsafe_allow_html=True)
            filter = st.sidebar.radio('Covert your photo to:', ['Original','Gray Image','Black and White', 'Pencil Sketch', 'Blur Effect'])
            if filter == 'Gray Image':
                    converted_img = np.array(image.convert('RGB'))
                    gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
                    filter_image=gray_scale
                    st.image(gray_scale, width=300)
            elif filter == 'Black and White':
                    converted_img = np.array(image.convert('RGB'))
                    gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
                    slider = st.sidebar.slider('Adjust the intensity', 1, 255, 127, step=1)
                    filter_image=gray_scale
                    (thresh, blackAndWhiteImage) = cv2.threshold(gray_scale, slider, 255, cv2.THRESH_BINARY)
                    st.image(blackAndWhiteImage, width=300)
            elif filter == 'Pencil Sketch':
                    converted_img = np.array(image.convert('RGB')) 
                    gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
                    inv_gray = 255 - gray_scale
                    slider = st.sidebar.slider('Adjust the intensity', 25, 255, 125, step=2)
                    blur_image = cv2.GaussianBlur(inv_gray, (slider,slider), 0, 0)
                    sketch = cv2.divide(gray_scale, 255 - blur_image, scale=256)
                    filter_image=blur_image
                    st.image(sketch, width=300) 
            elif filter == 'Blur Effect':
                    converted_img = np.array(image.convert('RGB'))
                    slider = st.sidebar.slider('Adjust the intensity', 5, 81, 33, step=2)
                    converted_img = cv2.cvtColor(converted_img, cv2.COLOR_RGB2BGR)
                    blur_image = cv2.GaussianBlur(converted_img, (slider,slider), 0, 0)
                    filter_image=blur_image
                    st.image(blur_image, channels='BGR', width=300) 
            else:
                    filter_image=image 
                    st.image(image, width=300) 
            
