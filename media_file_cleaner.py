import os
import pathlib
import re
from os import path

from file_cleaner_base import FileCleanerBase


class MediaFileCleaner(FileCleanerBase):

    def __init__(self, ignored_extensions, delete_dir):
        self.ignored_extensions = ignored_extensions
        self.delete_dir = delete_dir

    def try_clean_file(self, filename, rootDir):
        _, extension = os.path.splitext(filename)

        relative_path = os.path.relpath(filename, rootDir)

        should_clean = False

        if re.search(self.ignored_extensions, relative_path):
            should_clean = True

        if should_clean:
            dest = path.join(self.delete_dir, relative_path);
            self.clean_file(filename, dest)

        return should_clean

    def clean_file(self, filename, dest):
        print("move: " + filename + "\n\tto\n\t" + dest )
        dir_path = os.path.dirname(os.path.realpath(dest))
        pathlib.Path(dir_path).mkdir(parents=True, exist_ok=True)
        os.rename(filename, dest)


