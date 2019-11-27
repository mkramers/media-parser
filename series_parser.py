from os import path
import PTN
from tvdb_api import TvdbApiController

from parser import InfoGetter, ApiSearcher, RenamePathBuilder, MediaParserBase, MediaParser


class EpisodeResult:

    def __init__(self, name, season, episode, episode_title):
        self.name = name
        self.season = season
        self.episode = episode
        self.episode_title = episode_title


class SeriesInfoGetter(InfoGetter):

    def get_info(self, filepath):
        result = PTN.parse(filepath)

        return result


class SeriesApiSearcher(ApiSearcher):
    api = TvdbApiController()

    def get_api_result(self, info):
        found_info = self.api.find_episode_info(info)

        series_title = found_info["title"]
        episode_title = found_info["episodeName"]
        season = found_info["airedSeason"]
        episode = found_info["airedEpisodeNumber"]

        return EpisodeResult(series_title, season, episode, episode_title)


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
