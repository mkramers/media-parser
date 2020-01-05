from media_file_cleaner import MediaFileCleaner
from remove_empty_dirs import removeEmptyFolders
from series_media_parser import SeriesMediaParser
import os

def testMe():
    filepath = 'River.of.No.Return.S01E02.Bearing.Down.on.the.Ranch.720p.WEBRip.x264-CAFFEiNE[rarbg]\River.of.No.Return.S01E02.Bearing.Down.on.the.Ranch.720p.WEBRip.x264-CAFFEiNE.mkv'
    parser = SeriesMediaParser()

    result = parser.get_rename_path(filepath)
    print(result)


def main():
    rootDir = 'C:\seed\public'
    outputDir = 'F:\videos\TV Shows'
    deleteDir = 'C:\seed\_delete_me'
    
    ignored_extensions = "^(.*)\\Sample\\.*|(^.*\.(nfo|NFO|sfv|SFV|exe|EXE|txt|TXT|rar|RAR|r[0-9]{2}|R[0-9]{2})$)"

    parser = SeriesMediaParser()
    cleaner = MediaFileCleaner(ignored_extensions, deleteDir)

    files = getListOfFiles(rootDir);
    for file in files:
        if not cleaner.try_clean_file(file, rootDir):
            print("renaming " + file)
            # result = parser.get_rename_path(file)
            # print(result)

    # clean empty dirs
    removeEmptyFolders(rootDir, False)


def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


main()
