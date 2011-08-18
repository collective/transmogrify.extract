from setuptools import setup, find_packages

import os

setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    description='Extracts all content from within the specified CSS id or class',
    license='GPL',
    long_description=open('README.rst').read() +
        open(os.path.join('docs','HISTORY.txt')).read(),
    include_package_data=True,
    install_requires=[
        'lxml'
        'mr.migrator',
        'setuptools',
    ],
    name='transmogrify.extract',
    namespace_packages=[
        'transmogrify',
    ],
    packages=find_packages(),
    url='https://github.com/aclark4life/transmogrify.extract',
    version='0.0.1',
)
