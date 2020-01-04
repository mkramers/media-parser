from abc import ABC, abstractmethod


class InfoGetter(ABC):

    @abstractmethod
    def get_info(self, filepath):
        pass