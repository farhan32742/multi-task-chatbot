from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load all environment variables from .env
load_dotenv()

# Configuring API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro Vision Model and get response
def get_gemini_response(input, image, prompt):
    # Loading the model
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input, image[0], prompt])
    return response.text

# Function to summarize text using Gemini
def summarize_text(input_text):
    # Loading the model
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = "Please summarize the following text concisely."
    response = model.generate_content([input_text, prompt])
    return response.text

def sentiment_analysis(input_text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = "You are an expert in sentiment analysis. Given the input text, analyze and classify the sentiment as positive, negative, or neutral. Additionally, provide a brief explanation for your classification."
    response = model.generate_content([input_text,prompt])
    return response.text


# Function to prepare uploaded image for processing
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit Page Configuration
st.set_page_config(page_title="Gemini Application")

# Application Header
st.header("Gemini Application")

# User Input for Prompt and File Upload
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an Image...", type=["jpg", "jpeg", "png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

# Buttons for Invoice Analysis and Text Summarization
col1, col2 ,col3= st.columns(3)

with col1:
    submit_invoice = st.button("Tell me about the invoice")

with col2:
    submit_summary = st.button("Summarize Text")

with col3:
    submit_sentiment_analysis = st.button("sentiment_analysis")

input_prompt = """
You are an expert in understanding invoices. You will receive input images as invoices and you will have to answer questions based on the input image.
"""

# Handle "Tell me about the invoice" button
if submit_invoice:
    if uploaded_file:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_prompt, image_data, input)
        st.subheader("Invoice Analysis Response:")
        st.write(response)
    else:
        st.error("Please upload an image to analyze the invoice.")

# Handle "Summarize Text" button
if submit_summary:
    if input:
        summary_response = summarize_text(input)
        st.subheader("Summary Response:")
        st.write(summary_response)
    else:
        st.error("Please enter text for summarization.")
# Handle "Sentiment analysis " button
if submit_sentiment_analysis:
    if input:
        sentiment_respnce = sentiment_analysis(input)
        st.subheader("sentiment  Response:")
        st.write(sentiment_respnce)
    else:
        st.error("Please enter text for sentiment analysis.")

