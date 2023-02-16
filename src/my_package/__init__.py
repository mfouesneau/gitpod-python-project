from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("my_package")
except PackageNotFoundError:
    # package is not installed
    pass