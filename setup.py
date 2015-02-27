# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import info
import version

packages = [
    'coil'
]

with open('README.rst') as f:
    readme = f.read()

setup_options = info.INFO
setup_options["version"] = version.VERSION
setup_options.update(dict(
    packages=packages,
    install_requires=open('requirements.txt').read().splitlines(),
    test_suite='test_coil.suite',
    long_description=readme
))

setup(**setup_options)
