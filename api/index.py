import os
import sys

# Add Backend folder to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Backend'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_core.settings')

from clinic_core.wsgi import application

# Vercel Serverless Function Handler
app = application
