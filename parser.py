from abc import ABC, abstractmethod


def determine_media_type(filepath):
    return 0


class InfoGetter(ABC):

    @abstractmethod
    def get_info(self, filepath):
        pass


class ApiSearcher(ABC):

    @abstractmethod
    def get_api_result(self, info):
        pass


class RenamePathBuilder(ABC):

    @abstractmethod
    def build_rename_path(self, result):
        pass


class MediaParserBase(ABC):

    @abstractmethod
    def get_rename_path(self, filename):
        pass


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


