import sys

from setuptools import setup
import os


class LibrarySetup:
    def __init__(self):
        self.classifiers = [
            'Development Status :: 5 - Production/Stable',
            'Operating System :: Microsoft :: Windows :: Windows 10',
            'Programming Language :: Python :: 3'
        ]

        self.required_packages = [
            'colorama',
            'psutil'
        ]

        self.create_dist()
        self.upload_to_pypi()

    def create_dist(self):
        setup(
            name='procspy',
            version='1.0.0',
            description='ProcSpy - portable command prompt task manager',
            long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
            url='https://github.com/Bamboooz/procspy',
            author='Bamboooz',
            author_email='bambusixmc@gmail.com',
            license='MIT',
            classifiers=self.classifiers,
            keywords=['python', 'windows', 'linux', 'macos', 'cpu',
                      'temperature', 'motherboard', 'system-monitor',
                      'hardware-information', 'network-information'],
            packages=['prompt', 'procspy', 'scripts', 'sensor', 'stdout'],
            install_requires=self.required_packages
        )

    @staticmethod
    def upload_to_pypi():
        os.popen(r"twine upload --repository-url https:\\upload.pypi.org\legacy dist\*")


LibrarySetup()
