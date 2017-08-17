#!/usr/bin/env python

from setuptools import setup, find_packages
import alot


setup(
    name='alot',
    version=alot.__version__,
    description=alot.__description__,
    author=alot.__author__,
    author_email=alot.__author_email__,
    url=alot.__url__,
    license=alot.__copyright__,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console :: Curses',
        'Framework :: Twisted',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Communications :: Email :: Email Clients (MUA)',
    ],
    packages=find_packages(exclude=['tests*']),
    package_data={
        'alot': [
            'defaults/alot.rc.spec',
            'defaults/notmuch.rc.spec',
            'defaults/abook_contacts.spec',
            'defaults/default.theme',
            'defaults/default.bindings',
            'defaults/config.stub',
            'defaults/theme.spec',
        ]
    },
    entry_points={
        'console_scripts':
            ['alot = alot.__main__:main'],
    },
    install_requires=[
        'notmuch>=0.13',
        'urwid>=1.1.0',
        'urwidtrees>=1.0',
        'twisted>=10.2.0',
        'python-magic',
        'configobj>=4.7.0',
        'gpg'
    ],
    tests_require=[
        'mock',
    ],
    provides=['alot'],
    test_suite="tests",
)
