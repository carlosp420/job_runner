import os
import sys
sys.path.append('/data/carlos/job_runner/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'job_runner.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
print application
