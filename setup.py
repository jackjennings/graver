from setuptools import setup

from graver import __version__


setup(
    name='Graver',
    version=__version__,
    author='Jack Jennings',
    author_email='j@ckjennin.gs',
    packages=['graver'],
    url='http://github.com/jackjennings/graver',
    license='LICENSE',
    description='GLIF file format reader',
    long_description=open('README.rst').read()
)
