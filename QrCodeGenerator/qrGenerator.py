# Import QRCode from pyqrcode
from importlib.resources import path
import os
import pyqrcode
import png
from pyqrcode import QRCode
import streamlit as st
from PIL import Image
import cv2

from Utils.createFolder import create_images_folder


def qr_generator(s):

    # Generate QR code
    url = pyqrcode.create(s)
    z=create_images_folder()
    path = os.path.join(z, "myqr.png")
    # st.image(url.svg("myqr.svg", scale=8))
    url.png(path, scale=6)
    # # Create and save the png file naming "myqr.png"
    x=Image.open(path)
    st.image(x)

    from io import BytesIO
    buf = BytesIO()
    x.save(buf, format="JPEG")
    byte_im = buf.getvalue()
    btn = st.download_button(
        label="Download Image",
        data=byte_im,
        file_name="MYQRCODE.png",
        mime="image/jpeg",
    )
