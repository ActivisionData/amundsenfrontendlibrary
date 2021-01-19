import os

from typing import Dict, Optional
from flask import Flask
from amundsen_application.config import LocalConfig
from amundsen_application.models.user import load_user, User

# def get_access_headers(app: Flask) -> Optional[Dict]:
#     """
#     Function to retrieve and format the Authorization Headers
#     that can be passed to various microservices who are expecting that.
#     :param app: The instance of the current app.
#     :return: A formatted dictionary containing access token
#     as Authorization header.
#     """
#     try:
#         access_token = app.oidc.get_access_token()
#         return {'Authorization': 'Bearer {}'.format(access_token)}
#     except Exception:
#         return None

def get_auth_user(app: Flask) -> User:
    """
    Retrieves user info from the SAML attributes and creates a new User.
    :param app: The instance of the current app.
    :return: A class User
    """
    from flask import session
    attr = {}
    for k, v in session['saml']['attributes'].items():
        attr[k] = v[0]
    user_info = load_user(attr)
    return user_info

class SamlConfig(LocalConfig):
    AUTH_USER_METHOD = get_auth_user
    SECRET_KEY = os.urandom(24)
    SAML_METADATA_URL = os.environ.get("SAML_METADATA_URL", None)
    # REQUEST_HEADERS_METHOD = get_access_headers