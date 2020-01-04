import PTN

from info_getter import InfoGetter


class SeriesInfoGetter(InfoGetter):

    def get_info(self, filepath):
        result = PTN.parse(filepath)

        return result