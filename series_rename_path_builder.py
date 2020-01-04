from os import path

from rename_path_builder import RenamePathBuilder


class SeriesRenamePathBuilder(RenamePathBuilder):

    def prepend_episode(self, episode_number):
        return f"E{episode_number:02}"

    def build_rename_path(self, result):
        directory = path.join(result.name, f"Season {result.season:02}")

        if hasattr(result.episode, "__len__"):
            episodes = map(self.prepend_episode, result.episode)
            episode_string = "-".join(episodes)
        else:
            episode_string = self.prepend_episode(result.episode)

        filename = f"{result.name} - S{result.season:02}{episode_string} - {result.episode_title}.mkv"
        return path.join(directory, filename)