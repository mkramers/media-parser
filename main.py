from series_parser import SeriesMediaParser


def main():
    filepath = 'River.of.No.Return.S01E02.Bearing.Down.on.the.Ranch.720p.WEBRip.x264-CAFFEiNE[rarbg]\River.of.No.Return.S01E02.Bearing.Down.on.the.Ranch.720p.WEBRip.x264-CAFFEiNE.mkv'
    parser = SeriesMediaParser()
    result = parser.get_rename_path(filepath)
    print(result)


main()
