import sys

sys.path.insert(0, "/home/usercpanel/apps/django-blog")

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()