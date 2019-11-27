import requests


class TvdbApi:

    def find_episode_info(self, info):

        print(info)
        root_url = "https://api.thetvdb.com"

        series_title = info['title']

        login_url = f"{root_url}/login"

        content_type_headers = {'content-type': 'application/json'}
        login_data = {"apikey": "C603D7C458E29083", "username": "mkramesss", "userkey": "1LG5KYQABX1H43GH"}

        login_response = requests.post(url=login_url, headers=content_type_headers, json=login_data)
        login_response_json = login_response.json()

        jwt_token = login_response_json["token"]

        auth_headers = {'Authorization': "Bearer " + jwt_token}

        search_url = f"{root_url}/search/series"

        search_headers = content_type_headers.copy()
        search_headers.update(auth_headers)

        search_params = {'name': series_title}

        search_response = requests.get(url=search_url, headers=search_headers, params=search_params)

        search_response_json = search_response.json()

        series_id = search_response_json["data"][0]["id"]

        episode_info_url = f"{root_url}/series/{series_id}/episodes/query"
        episode_info_params = {'id': str(series_id), "airedSeason": str(info['season']), "airedEpisode": str(info['episode'])}

        episode_info_response = requests.get(url=episode_info_url, headers=search_headers, params=episode_info_params)

        episode_info_response_json = episode_info_response.json()

        info = episode_info_response_json["data"][0]

        title_info = {'title': series_title}
        info.update(title_info)

        return info
