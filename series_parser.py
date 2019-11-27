from os import path
import PTN
from tvdb_api import TvdbApi

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
        return SeriesInfo(result['title'], result['season'], result['episode'])


class SeriesApiSearcher(ApiSearcher):

    def get_api_result(self, info):

        api = TvdbApi()
        found_info = api.find_episode_info(info)

        episode_title = found_info["episodeName"]

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
