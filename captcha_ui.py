import streamlit as st
from captcha.image import ImageCaptcha
import random
import string
from PIL import Image

# Generate CAPTCHA
def create_captcha():
    text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    image = ImageCaptcha(width=280, height=90)
    image.write(text, "captcha.png")
    return text

# Session state
if "captcha" not in st.session_state:
    st.session_state.captcha = create_captcha()

# UI
st.set_page_config(page_title="CAPTCHA UI", page_icon="🔐")
st.title("🔐 CAPTCHA Verification")

st.image("captcha.png", caption="Enter the CAPTCHA shown")

user_input = st.text_input("Enter CAPTCHA")

col1, col2 = st.columns(2)

with col1:
    if st.button("Verify"):
        if user_input == st.session_state.captcha:
            st.success("✅ CAPTCHA Verified")
        else:
            st.error("❌ Wrong CAPTCHA")

with col2:
    if st.button("Refresh 🔄"):
        st.session_state.captcha = create_captcha()
        st.rerun()
