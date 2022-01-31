#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='thumbor-plugins-gifv',
    version='0.0.1',
    keywords='thumbor ffmpeg gifv mp4',
    author='Guilherme Souza',
    author_email='guilherme@souza.tech',
    url='https://thumbor.readthedocs.io/en/latest/index.html',
    license='MIT',
    description='Thumbor optimizer to add support to Gifv(mp4)',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Multimedia :: Graphics :: Presentation'
    ],
    packages=[
        'thumbor_plugins.optimizers.gifv',
        'thumbor_plugins',
    ],
    package_dir= {
        'thumbor_plugins': '../../..',
        'thumbor_plugins.optimizers.gifv': '.',
    },
    install_requires=[
        'webcolors==1.11.1',
    ],
)