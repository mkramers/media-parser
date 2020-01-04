from abc import ABC, abstractmethod


class ApiSearcher(ABC):

    @abstractmethod
    def get_api_result(self, info):
        pass