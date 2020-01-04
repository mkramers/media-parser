from series_media_parser import SeriesMediaParser
import os

def testMe():
    filepath = 'River.of.No.Return.S01E02.Bearing.Down.on.the.Ranch.720p.WEBRip.x264-CAFFEiNE[rarbg]\River.of.No.Return.S01E02.Bearing.Down.on.the.Ranch.720p.WEBRip.x264-CAFFEiNE.mkv'
    parser = SeriesMediaParser()
    result = parser.get_rename_path(filepath)
    print(result)


def main():
    parser = SeriesMediaParser()

    rootDir = 'C:\seed\public'
    for root, dirs, files in os.walk(rootDir):
        for file in files:
            print(os.path.join(root, file))
            result2 = parser.get_rename_path(file)
            print(result2)


main()


# iterate through dirs
# rename all files
# check if already exists
# confirm with user
