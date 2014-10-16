#!/usr/bin/env python

from setuptools import setup
setup(
    name='dragonbourne',
    version='0.0.1',
    description='a multi-user text adventure for your shell',
    url='https://github.com/lindboe/dragonbourne',
    author='Lizzi Lindboe, Nathaniel Smith',
    license='GPL',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Other Audience',
        'Topic :: Artistic Software',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    ],
    keywords='game',
    packages=['dragonbourne'],
    install_requires = ['pymongo==2.7.2', 'sh==1.09', 'pyyaml==3.11',],
)
