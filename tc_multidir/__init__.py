from thumbor.config import Config

from ._version import __version__

Config.define(
    "TC_MULTIDIR_PATHS",
    [],
    "The list of paths where the File Loader will try to find images",
    "File Loader",
)
