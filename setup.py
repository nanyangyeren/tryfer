from setuptools import setup

from twisted.python.dist import getPackages

setup(
    name='tryfer',
    version='0.1',
    description='Twisted Zipkin Tracing Library',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Framework :: Twisted'
    ],
    license='APL2',
    url='https://github.com/racker/tryfer',

    packages=getPackages('tryfer'),
    install_requires=['Twisted', 'thrift', 'scrivener'],
)
