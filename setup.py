# Upload package to PyPi.

from setuptools import setup

setup(name='schoolopy',
      version='0.1.1',
      description='Finally, a Python wrapper for Schoology\'s API.',
      url='https://github.com/ErikBoesen/schoolopy',
      author='Erik Boesen',
      author_email='me@erikboesen.com',
      license='MIT',
      packages=['schoolopy'],
      install_requires=[],
      zip_safe=False)
