#!/usr/bin/python3

from sys import exit
import os
import spigot
from pathlib import Path

artifact_build_path = Path.cwd().joinpath(
    os.getenv('SPIGOT_BUILD_PATH', 'BuildTools'))
artifact_build_type = os.getenv('SPIGOT_BUILD_TYPE', 'spigot')

spigot_jar = spigot.find_spigot_jar(artifact_build_path,
                                    f"{artifact_build_type}-*.jar")

if spigot_jar is None:
    print(f"Found no {artifact_build_type}-[...].jar file.")
    exit(1)

spigot_version = spigot.get_spigot_version(spigot_jar)

if spigot_version is None:
    print(f"Unable to parse version of Spigot.")
    exit(1)

print(f"::echo set-env SPIGOT_BUILD_OUTPUT_VERSION {spigot_version}")
spigot.dump_spigot_manifest(spigot_version, spigot_jar)