from media_file_cleaner import MediaFileCleaner
from series_media_parser import SeriesMediaParser
import os

def testMe():
    filepath = 'River.of.No.Return.S01E02.Bearing.Down.on.the.Ranch.720p.WEBRip.x264-CAFFEiNE[rarbg]\River.of.No.Return.S01E02.Bearing.Down.on.the.Ranch.720p.WEBRip.x264-CAFFEiNE.mkv'
    parser = SeriesMediaParser()

    result = parser.get_rename_path(filepath)
    print(result)


def main():
    rootDir = 'C:\seed\public'
    deleteDir = 'C:\seed\_delete_me'
    ignored_extensions = "^.\\\\Sample.*|(^.*\.(nfo|NFO|sfv|SFV|rar|RAR|r[0-9]{2}|R[0-9]{2})$)"

    parser = SeriesMediaParser()
    cleaner = MediaFileCleaner(ignored_extensions, deleteDir)

    for root, dirs, files in os.walk(rootDir):
        for file in files:
            print(os.path.join(root, file))
            if not cleaner.try_clean_file(file):
                result = parser.get_rename_path(file)
                print(result)
                print('...')


main()


# iterate through dirs
# rename all files
# check if already exists
# confirm with user
