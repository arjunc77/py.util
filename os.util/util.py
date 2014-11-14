#! /usr/bin/env python
import os


def get_ext_type_files_in_dir(dir_path, ext):
    """
    Return all file paths in the given 'dir_path'
    recursively with the extension 'ext'
    """
    join = os.path.join
    splitext = os.path.splitext
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            if splitext(f)[-1] == ext:
                yield join(root, f)
