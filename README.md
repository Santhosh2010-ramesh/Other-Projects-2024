# Other-Projects-2024
# Multi-Language Invoice Extractor

![Project Logo/Icon - Optional](D:\gemini.jpeg)

**Multi-Language Invoice Extractor** is a Python-based application that leverages the power of Google Gemini for extracting details from invoices in multiple languages. The application utilizes various libraries, including Streamlit, google-generativeai, python-dotenv, langchain, PyPDF2, and chromadb, to achieve efficient and accurate extraction of information.



## Features
- **Multi-Language Support:** Extract details from invoices written in various languages.
- **Google Gemini Integration:** Utilize the power of Google Gemini for accurate information extraction.
- **User-Friendly Interface:** Built with Streamlit, providing a simple and intuitive user interface.
- **Customizable Configuration:** Tailor the application to your needs using python-dotenv.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/multi-language-invoice-extractor.git

   Navigate to the project directory:

bash
Copy code
cd multi-language-invoice-extractor
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Ensure that your Google Gemini API credentials are set up and configured.
Create a .env file with the necessary configuration parameters (see Configuration).
Run the application using Streamlit:
bash
Copy code
streamlit run app.py
Open the provided URL in your web browser to access the application.
Libraries Used
Streamlit: A Python library for creating web applications with minimal effort.
google-generativeai: Interact with Google Gemini for invoice information extraction.
python-dotenv: Load environment variables from a .env file.
langchain: Library for language-related tasks.
PyPDF2: Read and extract text from PDF files.
chromadb: A library for interacting with a Chrome extension for data storage.
Configuration
Create a .env file in the project directory and provide the following configuration parameters:

dotenv
GOOGLE_GEMINI_API_KEY
OTHER_CONFIG_PARAM=value
...
Make sure to replace your_api_key_here with your actual Google Gemini API key and configure other parameters as needed.

Contributing
We welcome contributions! Feel free to open issues, submit pull requests, or provide feedback.

License
This project is licensed under the Santhosh Ramesh License - see the LICENSE file for details.

