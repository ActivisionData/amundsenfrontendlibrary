import logging

from flask import redirect, Flask, request, g, session, url_for
from urllib.parse import urlparse

LOGGER = logging.getLogger(__name__)

class FlaskSAML(Flask):

    def _before_request(self):
        passthrough = ['/saml/sso/', '/saml/acs/']
        if any(path in request.path for path in passthrough):
            pass
        elif 'saml' not in session:
            return redirect('/saml/sso/')
        else:
            LOGGER.debug(f"session: {session}")

    def __init__(self, *args, **kwargs):
        super(FlaskSAML, self).__init__(*args, **kwargs)

        # Register the before request function that will make sure each
        # request is authenticated before processing
        self.before_request(self._before_request)
