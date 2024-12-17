# MULTI-TASK Application

## Overview
The Gemini Application is a Streamlit-based web application designed to leverage the Gemini Pro Vision Model by Google. This app provides three core functionalities:

1. **Invoice Analysis**: Analyze uploaded invoice images and answer questions related to them.
2. **Text Summarization**: Summarize input text concisely.
3. **Sentiment Analysis**: Perform sentiment analysis on input text, classifying it as positive, negative, or neutral with a brief explanation.

---

## Features
### 1. Invoice Analysis
- Upload an image of an invoice.
- The application uses the Gemini Pro Vision Model to extract and analyze information from the uploaded invoice.

### 2. Text Summarization
- Input text in the provided field.
- Get a concise summary of the entered text.

### 3. Sentiment Analysis
- Input text in the provided field.
- Classify the sentiment of the text and receive a brief explanation.

---

## Prerequisites
### Dependencies
- Python 3.9 or above
- Required Python packages:
  - `streamlit`
  - `Pillow`
  - `python-dotenv`
  - `google-generativeai`

### Environment Variables
- A `.env` file with the following variable:
  ```env
  GOOGLE_API_KEY=your_google_api_key
  ```

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   - Create a `.env` file in the project directory.
   - Add your Google API Key:
     ```
     GOOGLE_API_KEY=your_google_api_key
     ```

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```

---

## Usage
1. Launch the application in your browser.
2. Use the text input field to provide prompts or text for summarization/sentiment analysis.
3. Upload images in `.jpg`, `.jpeg`, or `.png` format for invoice analysis.
4. Click the respective buttons to execute the desired functionality:
   - **Tell me about the invoice**: For invoice analysis.
   - **Summarize Text**: For text summarization.
   - **Sentiment Analysis**: For sentiment classification.

---

## File Structure
```
project_directory/
├── app.py                 # Main application code
├── .env                   # Environment variables (not included in the repository)
├── requirements.txt       # List of dependencies
└── README.md              # Documentation
```

---

## API Integration
The application uses the Gemini Pro Vision Model via the `google-generativeai` library. Ensure that you have the correct API key configured in the `.env` file.

### Key Methods:
1. **get_gemini_response**: Processes invoice images and generates a response based on a prompt.
2. **summarize_text**: Summarizes input text.
3. **sentiment_analysis**: Analyzes the sentiment of input text.

---

## Streamlit Page Configuration
- **Page Title**: "Gemini Application"
- **Header**: "Gemini Application"
- **Layout**: Three interactive columns for the main functionalities.

---

## Troubleshooting
1. **Missing API Key**: Ensure the `.env` file is correctly configured with your Google API Key.
2. **File Upload Errors**: Verify the uploaded file is in the supported formats (`.jpg`, `.jpeg`, `.png`).
3. **Streamlit Not Running**: Ensure all dependencies are installed and the correct Python version is being used.

---

## Future Enhancements
- Add support for additional image formats.
- Improve error handling and validation.
- Extend functionalities to include additional text and image analysis capabilities.

---

## Acknowledgments
- [Google Generative AI](https://developers.generativeai.google/) for providing the Gemini Pro Vision Model.
- [Streamlit](https://streamlit.io/) for an interactive UI framework.

