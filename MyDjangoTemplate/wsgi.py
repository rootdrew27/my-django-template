import os
from pathlib import Path
from django.core.wsgi import get_wsgi_application

PROJECT_NAME = (str(Path(__file__).resolve().parent)).split('\\')[-1] # returns the directory which contains this file (ie the the Project's Name)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', PROJECT_NAME + '.settings')

application = get_wsgi_application()
