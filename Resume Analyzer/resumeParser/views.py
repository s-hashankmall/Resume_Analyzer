import os
import spacy
import PyPDF2
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
import cohere

# Load SpaCy model for NER
nlp = spacy.load('en_core_web_sm')

# Cohere API Client setup
cohere_client = cohere.Client('YOUR_COHERE_API_KEY')


#extract the text from the resume 
def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file"""
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text

#extract skills from the text
def extract_skills(text):
    """Extract technical skills using NER"""
    doc = nlp(text)
    skills = set()  # Using set to avoid duplicates
    for ent in doc.ents:
        # print(f"Entity: {ent.text}, Label: {ent.label_}")
        if ent.label_ == 'SKILL':  # Assuming the 'SKILL' label exists
            skills.add(ent.text)

    return skills



#from the extracted skills suggest the suitable job_roles
def suggest_job_roles(skills):
    """Generate job role suggestions using Cohere API"""
    prompt = (f"Generate two or three job roles for a candidate with these technical skills: {', '.join(skills)}. "
              "Use specific skills to match job roles. For example, Python and Django could suggest a 'Django Web Developer'. "
              "Linux and DevOps could suggest a 'DevOps Engineer'. Avoid repeating roles like Data Analyst."
              "Just give the names of that role don't describe that. for example for role of Python Full Stack Developer simply write Python Full Stack Developer")
    response = cohere_client.generate(
        model='command-xlarge-nightly',
        prompt=prompt,
        max_tokens=100
    )
    return response.generations[0].text.strip()





def parse_resume(request):
    if request.method == 'POST':
        resume = request.FILES['resume']
        file_path = default_storage.save(f'temp/{resume.name}', resume)

        # Extract text from the uploaded PDF
        full_path = os.path.join(default_storage.location, file_path)
        resume_text = extract_text_from_pdf(full_path)

        # Extract technical skills using NER
        skills = extract_skills(resume_text)
        
        # Generate job role suggestions based on the extracted skills
        job_roles = suggest_job_roles(skills)

        # Clean up the temp file
        default_storage.delete(file_path)

        # Render the result
        return render(request, 'job_roles.html', {'skills': skills, 'job_roles': job_roles})

    return redirect('/')


def upload_resume(request):
    return render(request, 'upload_resume.html')