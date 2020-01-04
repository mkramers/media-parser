from media_parser_base import MediaParserBase
from media_parser import MediaParser
from series_api_searcher import SeriesApiSearcher
from series_info_getter import SeriesInfoGetter
from series_rename_path_builder import SeriesRenamePathBuilder


class SeriesMediaParser(MediaParserBase):

    def get_rename_path(self, filename):
        info_getter = SeriesInfoGetter()
        api_searcher = SeriesApiSearcher()
        rename_path_builder = SeriesRenamePathBuilder()

        parser = MediaParser(info_getter, api_searcher, rename_path_builder)

        return parser.get_rename_path(filename)