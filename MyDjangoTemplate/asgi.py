from pathlib import Path
import os
from django.core.asgi import get_asgi_application

PROJECT_NAME = (str(Path(__file__).resolve().parent)).split('\\')[-1] # returns the directory which contains this file (ie the the Project's Name)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', PROJECT_NAME + '.settings')

application = get_asgi_application()
