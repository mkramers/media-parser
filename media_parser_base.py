from abc import ABC, abstractmethod


class MediaParserBase(ABC):

    @abstractmethod
    def get_rename_path(self, filename):
        pass