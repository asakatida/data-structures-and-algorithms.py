from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md')) as f:
    README = f.read()

setup(
    name='grandquista-data-structures-and-algorithms',
    version='1.0.0',

    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    author_email='grandquista@gmail.com',
    author='Adam Grandquist',
    description=''.join(README.splitlines()[:7]),
    extras_require={
        'testing': ['pytest'],
    },
    keywords='whiteboard data structures',
    long_description=README,
    packages=find_packages(),
    setup_requires=['pytest-runner'],
    url='https://github.com/grandquista/data-structures-and-algorithms',
)
