from media_parser_base import MediaParserBase


class MediaParser(MediaParserBase):

    def __init__(self, info_getter, api_searcher, rename_path_builder):
        self.info_getter = info_getter
        self.api_searcher = api_searcher
        self.rename_path_builder = rename_path_builder

    def get_rename_path(self, filename):
        info = self.info_getter.get_info(filename)

        result = self.api_searcher.get_api_result(info)

        rename_path = self.rename_path_builder.build_rename_path(result)

        return rename_path


