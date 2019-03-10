from setuptools import setup
import puretransport


setup(
    name="pure-transport",
    version=puretransport.__version__,
    author='Devin Stevenson',
    description="Pure Sasl Based Thrift Transport for PyHive",
    long_description=
"""This package provides a thrift_transport for hive connections
using PyHive. This is mainly beneficial as an implementation of Pure-SASL
for Windows users where SASL is difficult to install. The other use case facilitated 
is support for SSL Sockets, however it is left for the user to configure the socket.""",
    license='GPLv3+',
    url="https://github.com/devinstevenson/pure-transport",
    keywords='pyhive',
    packages=['puretransport'],
    install_requires=['thrift', 'pure-sasl>=0.3.0', 'thrift-sasl'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ]
)
