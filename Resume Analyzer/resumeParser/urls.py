from django.urls import path
from resumeParser.views import *

urlpatterns = [
    path('', upload_resume, name='upload_resume'),
    path('parse_resume/', parse_resume, name='parse_resume'),
]
