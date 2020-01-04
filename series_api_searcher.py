from episode_result import EpisodeResult
from api_searcher import ApiSearcher
from tvdb_api_controller import TvdbApiController


class SeriesApiSearcher(ApiSearcher):
    api = TvdbApiController()

    def get_api_result(self, info):
        found_info = self.api.find_episode_info(info)

        series_title = found_info["title"]
        episode_title = found_info["episodeName"]
        season = found_info["airedSeason"]
        episode = found_info["airedEpisodeNumber"]

        return EpisodeResult(series_title, season, episode, episode_title)