import sys,os

os.environ['DJANGO_SETTINGS_MODULE'] = 'code_project.settings'
  
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
