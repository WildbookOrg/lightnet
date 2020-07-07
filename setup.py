# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
from pkg_resources import get_distribution, DistributionNotFound


def get_dist(pkgname):
    try:
        return get_distribution(pkgname)
    except DistributionNotFound:
        return None


requirements = [
    'numpy',
    'torchvision',
    'wbia-brambox',
]


setup_kwargs = dict(
    name='wbia-lightnet',
    author='EAVISE, WildMe Developers',
    author_email='dev@wildme.org',
    description='Building blocks for recreating darknet networks in pytorch',
    long_description=open('README.md').read(),
    # The following settings retreive the version from git.
    # See https://github.com/pypa/setuptools_scm/ for more information
    setup_requires=['setuptools_scm'],
    use_scm_version={
        'write_to': 'lightnet/_version.py',
        'write_to_template': '__version__ = "{version}"',
        'tag_regex': '^(?P<prefix>v)?(?P<version>[^\\+]+)(?P<suffix>.*)?$',
        'local_scheme': 'dirty-tag',
    },
    packages=find_packages(),
    test_suite='test',
    install_requires=requirements,
    extras_require={'visual': ['visdom']},
)


if __name__ == '__main__':
    setup(**setup_kwargs)
