import os

import requests
import datetime
import json

tvdb_root_url = "https://api.thetvdb.com"


def get_default_headers():
    content_type_headers = {'content-type': 'application/json'}

    return content_type_headers


class TvdbApi:

    def get_auth_headers(self, jwt_token):
        auth_token = {'Authorization': "Bearer " + jwt_token['token']}

        auth_headers = get_default_headers()
        auth_headers.update(auth_token)

        return auth_headers

    def get_series_result(self, jwt_token, info):
        series_title = info['title']
        auth_headers = self.get_auth_headers(jwt_token)
        search_params = {'name': series_title}
        search_url = f"{tvdb_root_url}/search/series"

        search_response = requests.get(url=search_url, headers=auth_headers, params=search_params)

        search_response_json = search_response.json()
        series_result = search_response_json["data"][0]

        return series_result

    def get_episode_result(self, jwt_token, parse_result, series_result):
        series_id = series_result["id"]
        series_title = series_result['seriesName']

        auth_headers = self.get_auth_headers(jwt_token)

        episode_info_params = {'id': str(series_id), "airedSeason": str(parse_result['season']),
                               "airedEpisode": str(parse_result['episode'])}
        episode_info_url = f"{tvdb_root_url}/series/{series_id}/episodes/query"
        episode_info_response = requests.get(url=episode_info_url, headers=auth_headers, params=episode_info_params)
        episode_info_response_json = episode_info_response.json()

        episode_result = episode_info_response_json["data"][0]

        # embed series title for future use
        title_info = {'title': series_title}
        episode_result.update(title_info)

        return episode_result

    def find_episode_info(self, parse_result, jwt_token):
        series_result = self.get_series_result(jwt_token, parse_result)

        episode_result = self.get_episode_result(jwt_token, parse_result, series_result, )

        return episode_result


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


class TvdbApiController:

    def __init__(self):
        self.api = TvdbApi()
        self.token_controller = TvdbApiTokenController()

    def find_episode_info(self, parse_result):
        jwt_token = self.token_controller.get_auth_token()
        episode_result = self.api.find_episode_info(parse_result, jwt_token)
        return episode_result
