import os

from django.core.wsgi import get_wsgi_application

# Tell Django to use your specific settings file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'budget_buddy.settings')

# This is the 'application' variable Gunicorn was looking for!
application = get_wsgi_application()