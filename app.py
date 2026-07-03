import streamlit as st
import cv2
import numpy as np

st.title("🖼️ Image to Sketch Converter")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    invert = 255 - gray

    blur = cv2.GaussianBlur(invert, (21, 21), 0)

    inverted_blur = 255 - blur

    sketch = cv2.divide(gray, inverted_blur, scale=256.0)

    st.subheader("Original Image")
    st.image(img, channels="BGR")

    st.subheader("Sketch")
    st.image(sketch)

    _, buffer = cv2.imencode(".png", sketch)

    st.download_button(
        label="⬇️ Download Sketch",
        data=buffer.tobytes(),
        file_name="sketch.png",
        mime="image/png"
    )