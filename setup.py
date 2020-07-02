# -*- coding: utf-8 -*-
from setuptools import find_packages, setup


def get_dist(pkgname):
    try:
        return get_distribution(pkgname)
    except DistributionNotFound:
        return None


def parse_version(fpath):
    """
    Statically parse the version number from a python file

    """
    import ast
    from os.path import exists

    if not exists(fpath):
        raise ValueError('fpath={!r} does not exist'.format(fpath))
    with open(fpath, 'r') as file_:
        sourcecode = file_.read()
    pt = ast.parse(sourcecode)

    class VersionVisitor(ast.NodeVisitor):
        def visit_Assign(self, node):
            for target in node.targets:
                if getattr(target, 'id', None) == '__version__':
                    self.version = node.value.s

    visitor = VersionVisitor()
    visitor.visit(pt)
    return visitor.version


requirements = [
    'numpy',
    'torchvision',
    'wbia-brambox',
]


setup_kwargs = dict(
    name='wbia-lightnet',
    version=parse_version('lightnet/__init__.py'),
    author='EAVISE, WildMe Developers',
    author_email='dev@wildme.org',
    description='Building blocks for recreating darknet networks in pytorch',
    long_description=open('README.md').read(),
    packages=find_packages(),
    test_suite='test',
    install_requires=requirements,
    extras_require={'visual': ['visdom']},
)


if __name__ == '__main__':
    setup(**setup_kwargs)
