# -*- coding: utf-8 -*-
#

import os

from setuptools import find_packages, setup

readme = open('README.md').read()

extras_require = {
    'tests': [
    'click==7.1.2',
        'pytest==4.6.11',
        'six==1.16.0',
    ]
}

setup_requires = [
    'pytest-runner>=3.0.0,<5',
]

install_requires = [
    'click==7.1.2',
    'six==1.16.0',
]

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('test1', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='test1',
    version=version,
    description=__doc__,
    long_description=readme,
    long_description_content_type='text/markdown',
    keywords='test',
    license='MIT',
    author='th22.net',
    author_email='hlava@cesnet.cz',
    url='https://github.com/thlava-cesnet/test1',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
#    platforms='any',
#    entry_points={},
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=extras_require['tests'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Development Status :: 3 - Alpha',
        # 'Development Status :: 5 - Production/Stable',
    ],
)
