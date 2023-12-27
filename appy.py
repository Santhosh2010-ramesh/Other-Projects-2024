from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load Gemini Pro Vision

model=genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input,Image,prompt):
    response=model.generate_content([input,Image[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:

        bytes_data=uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File uploaded")

#Initialize the Streamlit app
st.set_page_config(page_title="MultiLanguage Invoice Extractor")

st.header("MultiLanguage Invoice Extractor")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file=st.file_uploader("Choose an image of the invoice...",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image.",use_column_width=True)

submit=st.button("Tell me about the invoice")

input_prompt="""
You are an Expert in understanding invoices. We will upload an image as invoice and you wiill have to answer any questions based on the uploaded invooice image
"""
#if submit button is clicked
if submit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)