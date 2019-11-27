from os import path
import PTN
import requests
import urllib.parse

from parser import InfoGetter, ApiSearcher, RenamePathBuilder, MediaParserBase, MediaParser


class SeriesInfo:

    def __init__(self, name, season, episode):
        self.name = name
        self.season = season
        self.episode = episode


class SeriesResult:

    def __init__(self, name, year, season, episode, episode_title):
        self.name = name
        self.year = year
        self.season = season
        self.episode = episode
        self.episode_title = episode_title


class SeriesInfoGetter(InfoGetter):

    def get_info(self, filepath):
        result = PTN.parse(filepath)
        print(result)
        return SeriesInfo(result['title'], result['season'], result['episode'])


class SeriesApiSearcher(ApiSearcher):

    def get_api_result(self, info):
        root_url = "https://api.thetvdb.com"

        login_url = urllib.parse.urljoin(root_url, "login")

        content_type_headers = {'content-type': 'application/json'}
        login_data = {"apikey": "C603D7C458E29083", "username": "mkramesss", "userkey": "1LG5KYQABX1H43GH"}

        login_response = requests.post(url=login_url, headers=content_type_headers, json=login_data)
        login_response_json = login_response.json()

        jwt_token = login_response_json["token"]

        auth_headers = {'Authorization': "Bearer " + jwt_token}

        search_url = urllib.parse.urljoin(root_url, "search/series")

        search_headers = content_type_headers.copy()
        search_headers.update(auth_headers)

        search_params = {'name': info.name}

        search_response = requests.get(url=search_url, headers=search_headers, params=search_params)

        search_response_json = search_response.json()

        series_id = search_response_json["data"][0]["id"]

        episode_info_url = f"{root_url}/series/{series_id}/episodes/query"
        episode_info_params = {'id': str(series_id), "airedSeason": str(info.season), "airedEpisode": str(info.episode)}

        episode_info_response = requests.get(url=episode_info_url, headers=search_headers, params=episode_info_params)

        episode_info_response_json = episode_info_response.json()

        episode_title = episode_info_response_json["data"][0]["episodeName"]

        return SeriesResult(info.name, 1989, info.season, info.episode, episode_title)


class SeriesRenamePathBuilder(RenamePathBuilder):

    def prepend_episode(self, episode_number):
        return f"E{episode_number:02}"

    def build_rename_path(self, result):
        directory = path.join(result.name, f"Season {result.season:02}")

        if hasattr(result.episode, "__len__"):
            episodes = map(self.prepend_episode, result.episode)
            episode_string = "-".join(episodes)
        else:
            episode_string = self.prepend_episode(result.episode)

        filename = f"{result.name} - S{result.season:02}{episode_string} - {result.episode_title}.mkv"
        return path.join(directory, filename)


class SeriesMediaParser(MediaParserBase):

    def get_rename_path(self, filename):
        info_getter = SeriesInfoGetter()
        api_searcher = SeriesApiSearcher()
        rename_path_builder = SeriesRenamePathBuilder()

        parser = MediaParser(info_getter, api_searcher, rename_path_builder)

        return parser.get_rename_path(filename)
