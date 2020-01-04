from tvdb_api import TvdbApi
from tvdb_api_token_controller import TvdbApiTokenController


class TvdbApiController:

    def __init__(self):
        self.api = TvdbApi()
        self.token_controller = TvdbApiTokenController()

    def find_episode_info(self, parse_result):
        jwt_token = self.token_controller.get_auth_token()
        episode_result = self.api.find_episode_info(parse_result, jwt_token)
        return episode_result