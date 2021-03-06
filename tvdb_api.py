import requests

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


