import datetime
import json
import os

import requests

from tvdb_api import get_default_headers, tvdb_root_url


class TvdbApiTokenController:

    def __init__(self):
        self.token_file_path = "./token.json"
        self.jwt_token = None

    def get_auth_token_from_api(self):
        content_type_headers = get_default_headers()
        login_url = f"{tvdb_root_url}/login"
        login_data = {"apikey": "C603D7C458E29083", "username": "mkramesss", "userkey": "1LG5KYQABX1H43GH"}

        login_response = requests.post(url=login_url, headers=content_type_headers, json=login_data)
        login_response_json = login_response.json()

        jwt_token = login_response_json["token"]

        return {'token': jwt_token, 'expires': datetime.datetime.now() + datetime.timedelta(hours=24)}

    def save_token(self):
        with open(self.token_file_path, 'w') as fp:
            json.dump(self.jwt_token, fp, indent=4, sort_keys=True, default=str)

    def load_token(self):
        with open(self.token_file_path, 'r') as f:
            token = json.load(f)
            return token

    def load_or_create_token(self):
        create_new_token = True

        if os.path.isfile(self.token_file_path):
            self.jwt_token = self.load_token()

            if self.is_token_valid():
                create_new_token = False

        if create_new_token:
            self.jwt_token = self.get_auth_token_from_api()
            self.save_token()

    def get_auth_token(self):
        if not self.is_token_valid():
            self.load_or_create_token()

        return self.jwt_token

    def is_token_valid(self):
        valid = False

        if self.jwt_token is not None:
            expires = self.jwt_token['expires']
            if isinstance(expires, str):
                expires = datetime.datetime.strptime(expires, '%Y-%m-%d %H:%M:%S.%f')

            if datetime.datetime.now() < expires:
                valid = True

        return valid