import os
from os import path

from file_cleaner_base import FileCleanerBase


class MediaFileCleaner(FileCleanerBase):

    def __init__(self, ignored_extensions, delete_dir):
        self.ignored_extensions = ignored_extensions
        self.delete_dir = delete_dir

    def try_clean_file(self, filename):
        filename, extension = os.path.splitext(filename)

        cleaned = False
        if extension in self.ignored_extensions:
            self.clean_file(filename)
            cleaned = True

        return cleaned

    def clean_file(self, filename):
        destinsationFilename = path.join(self.delete_dir, filename);
        self.move_to_delete_dir(destinsationFilename, filename)

    def move_to_delete_dir(self, destinsationFilename, filename):
        print("cleaning: " + destinsationFilename)
        # os.rename(filename, destinsationFilename)

