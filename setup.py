from setuptools import find_packages, setup


def get_dist(pkgname):
    try:
        return get_distribution(pkgname)
    except DistributionNotFound:
        return None

def get_version():
    with open('VERSION', 'r') as f:
        version = f.read().splitlines()[0]
    with open('lightnet/version.py', 'w') as f:
        f.write('#\n')
        f.write('#   Lightnet version: Automatically generated version file\n')
        f.write('#\n\n')
        f.write(f'__version__ = "{version}"\n')

    return version


requirements = [
    'numpy',
    'torchvision',
    'wbia-brambox',
]


setup_kwargs = dict(
    name='wbia-lightnet',
    version=get_version(),
    author='EAVISE, WildMe Developers',
    author_email='dev@wildme.org',
    description='Building blocks for recreating darknet networks in pytorch',
    long_description=open('README.md').read(),
    packages=find_packages(),
    test_suite='test',
    install_requires=requirements,
    extras_require={
        'visual': ['visdom']
    },
)


if __name__ == '__main__':
    setup(**setup_kwargs)
