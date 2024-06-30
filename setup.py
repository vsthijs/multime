from setuptools import setup
from multime import __VERSION__ as version

setup(
    name="multime",
    version=version,
    entry_points={"console_scripts": ["multime=multime.__main__:main"]},
)
