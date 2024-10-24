Django Project:  
Resume Job Role Suggestion  
This project takes a resume as input, extracts the technical skills using Named Entity Recognition (NER), and suggests potential job roles using the Cohere API.  

Features  
-Upload a resume in PDF format.  
-Extract technical skills from the resume using SpaCy's NER.  
-Generate suggested job roles based on the extracted skills using the Cohere API.  

Requirements  
-Python 3.x  
-Django 4.x  
-Cohere API key (to be updated in the project)  


Before running the project, you must set up a virtual environment to manage the dependencies.  
-Command to create Virtual Environment ---      python3 -m venv env  
-Command to activate Virtual Environment---    .\env\Scripts\activate  


Once the virtual environment is activated, install the required packages by running:  pip install -r requirements.txt  



Update the Cohere API Key  
-This project uses the Cohere API for job role suggestions. You'll need to replace the placeholder API key with your own.  

Get your API key by signing up at Cohere.  
-Open the .env file (or wherever the API key is stored) in the root directory.  
-Replace the placeholder YOUR_COHERE_API_KEY with your own key  



Run the Project: py manage.py runserver  




Usage:  
-Visit the homepage to upload a resume.  
-The project will extract technical skills and provide suggested job roles based on the resume.  
