from os import path

from parser import InfoGetter, ApiSearcher, RenamePathBuilder, MediaParserBase, MediaParser


class SeriesInfo:

    def __init__(self, name, year, season, episode):
        self.name = name
        self.year = year
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
        return SeriesInfo("seriesName", 1989, 1, 1)


class SeriesApiSearcher(ApiSearcher):

    def get_api_result(self, info):
        return SeriesResult(info.name, info.year, info.season, info.episode, "Episode Title")


class SeriesRenamePathBuilder(RenamePathBuilder):

    def build_rename_path(self, result):
        directory = path.join(result.name, f"Season {result.season:02}")
        filename = f"{result.name} - S{result.season:02}E{result.episode:02} - {result.episode_title}.mkv"
        return path.join(directory, filename)


class SeriesMediaParser(MediaParserBase):

    def get_rename_path(self, filename):
        info_getter = SeriesInfoGetter()
        api_searcher = SeriesApiSearcher()
        rename_path_builder = SeriesRenamePathBuilder()

        parser = MediaParser(info_getter, api_searcher, rename_path_builder)

        return parser.get_rename_path(filename)
