import os
from setuptools import setup, find_packages

requires = [
    'pytz',
    'requests',
    'redis>=3.3.6',
    'pycryptodome==3.12.0',
    'xmltodict==0.12.0'
    ]

PACKAGE = 'VWeCom'
TOPDIR = os.path.dirname(__file__) or "."
VERSION = __import__(PACKAGE).__version__

setup(
    name = "veadoc-wecom-sdk",
    version = VERSION,
    keywords = ['wechat', 'wecom','workwechat','wxwork'],
    description = "SDK for Wecom API",
    long_description = "",
    license = "MIT Licence",

    url = "https://veadoc.com",
    author = "VEADoc",
    author_email = "1126@veadoc.me",

    packages = find_packages(exclude=["tests*"]), 
    include_package_data = True,
    platforms = "any",
    install_requires = requires,
        classifiers=[
        'Development Status :: 0 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        
    ]
)

