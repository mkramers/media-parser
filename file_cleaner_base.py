from abc import ABC, abstractmethod


class FileCleanerBase(ABC):

    @abstractmethod
    def try_clean_file(self, filename):
        pass