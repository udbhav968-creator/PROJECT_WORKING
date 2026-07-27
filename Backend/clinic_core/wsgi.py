import os
import sys
from pathlib import Path

# Add the Backend directory to sys.path so Django can find clinic_core and apps
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_core.settings')

from django.core.wsgi import get_wsgi_application  # noqa: E402

application = get_wsgi_application()

# Vercel entrypoint alias
app = application
