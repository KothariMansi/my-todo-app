from PIL import Image

import streamlit as st
def convert_image(input_image):
    """Gets a PIL image file and returns its grayscale version"""
    # Create a Pillow image instances
    img = Image.open(input_image)
    # Convert pillow image to gray_scale
    gray_img = img.convert('L')
    return gray_img
