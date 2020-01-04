import os
import re
from os import path

from file_cleaner_base import FileCleanerBase


class MediaFileCleaner(FileCleanerBase):

    def __init__(self, ignored_extensions, delete_dir):
        self.ignored_extensions = ignored_extensions
        self.delete_dir = delete_dir

    def try_clean_file(self, filename):
        filename, extension = os.path.splitext(filename)

        should_clean = False

        if re.search(self.ignored_extensions, filename):
            should_clean = True

        if should_clean:
            dest = path.join(self.delete_dir, filename);
            self.clean_file(filename, dest)

        return should_clean

    def clean_file(self, filename, dest):
        print("cleaning: " + dest)
        # os.rename(filename, dest)


