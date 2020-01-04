from abc import ABC, abstractmethod


class RenamePathBuilder(ABC):

    @abstractmethod
    def build_rename_path(self, result):
        pass