import sae
from IOS import wsgi

application = sae.create_wsgi_app(wsgi.application)