import os
import io
import shutil
import zipfile
from glob import glob
import json
from pathlib import PurePath, Path
import re
from distutils.version import StrictVersion

# Consts
artifact_name_pattern = re.compile(
    '([\w]+-)([0-9]+\.[0-9]+(?:\.[0-9]+)?)(.jar)', re.IGNORECASE)


def find_all(dir=None, glob_match='spigot-*.jar', verbose=False):
    valid_jars = []

    if dir is None:
        dir = Path.cwd()

    f_glob = sorted(dir.glob(glob_match))

    if f_glob is None or len(f_glob) == 0:
        return None

    for f in f_glob:
        f_name = f.name
        if verbose: print(f"Testing {f_name}", end='')
        f_match = artifact_name_pattern.match(f_name)

        if f_match is None:
            if verbose: print(" FAIL")
        else:
            valid_jars.append(f)
            if verbose: print(" OK")

    return sorted(valid_jars, key=lambda s: s.name)