import streamlit as st
from covertor import convert_image

#st.slider("Amount", min_value=10 , max_value=50)

#user_choice = st.radio("Amount",options=[10,20,30])
#if user_choice == 30:
#    st.info("You got it")

from PIL import Image

st.subheader("Color to grayscale Converter")

uploaded_image = st.file_uploader("Upload Image")


with st.expander("Start_camera"):
    camera_image = st.camera_input("Camera")

#Check if the image exists meaning the user has uploaded a file
if uploaded_image:
    gray_img = convert_image(uploaded_image)
    st.image(gray_img)



if camera_image:
    gray_img = convert_image(camera_image)

    st.image(gray_img)

