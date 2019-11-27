from unittest import TestCase

from series_parser import SeriesInfoGetter, SeriesInfo


class TestSeriesInfoGetter(TestCase):

    def test_get_info(self):
        tests = [
            (
            'River.of.No.Return.S01E02.Bearing.Down.on.the.Ranch.720p.WEBRip.x264-CAFFEiNE[rarbg]\River.of.No.Return.S01E02.Bearing.Down.on.the.Ranch.720p.WEBRip.x264-CAFFEiNE.mkv',
            SeriesInfo("River of No Return", 1, 2)),
            ('Greys.Anatomy.S16E03.WEBRip.x264-ION10\Greys.Anatomy.S16E03.WEBRip.x264-ION10.mp4',
             SeriesInfo("Greys Anatomy", 16, 3)),
            ('My.Horror.Story.S01E02.The.Devil.Inside.WEB.x264-CAFFEiNE.mkv', SeriesInfo("My Horror Story", 1, 2)),
            (
            'The.Dead.Files.S13E12.Absorbed.720p.WEBRip.x264-DHD[rarbg]\The.Dead.Files.S13E12.Absorbed.720p.WEBRip.x264-DHD.mkv',
            SeriesInfo("The Dead Files", 13, 12)),
            ('The.Affair.S05E03.WEBRip.x264-ION10\The.Affair.S05E03.WEBRip.x264-ION10.mp4',
             SeriesInfo("The Affair", 5, 3)),
            (
            'Jersey.Shore.Family.Vacation.S02E25.Tuxedo.Time.HDTV.x264-CRiMSON[rarbg]\Jersey.Shore.Family.Vacation.S02E25.Tuxedo.Time.HDTV.x264-CRiMSON.mkv',
            SeriesInfo("Jersey Shore Family Vacation", 2, 25)),
        ]
        for value, expected in tests:
            with self.subTest(value=value):
                info_getter = SeriesInfoGetter()
                result = info_getter.get_info(value)
                with self.subTest(msg="name does not match", result=result):
                    self.assertEqual(result.name, expected.name)
                with self.subTest(msg="season does not match", result=result):
                    self.assertEqual(result.season, expected.season)
                with self.subTest(msg="episode does not match", result=result):
                    self.assertEqual(result.episode, expected.episode)
