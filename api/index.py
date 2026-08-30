import os
import sys

backend_path = os.path.join(os.path.dirname(__file__), '..', 'Backend')
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_core.settings')

from clinic_core.wsgi import application

app = application
handler = application
