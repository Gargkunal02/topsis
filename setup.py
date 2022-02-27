from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.13'
DESCRIPTION = 'Streaming video data via networks'

# Setting up
setup(
    name="KunalGarg_101903683",
    version=VERSION,
    author="NeuralNine (Florian Dedov)",
    author_email="<mail@neuralnine.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['pandas','numpy','math','copy','sys','os'],
    classifiers=["Programming Language :: Python :: 3"]
)