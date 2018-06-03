from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='oevgk18_backend',
    version='0.0.1',
    description='API-Backend for ÖV-Güteklassen 2018',
    long_description=readme,
    author='Jonas Matter, Robin Suter',
    author_email='robin@robinsuter.ch',
    url='https://github.com/public-transport-quality-grades/backend',
    license="MIT License",
    packages=find_packages(exclude=('tests')),
    install_requires=['flask', 'flasgger', 'marshmallow', 'apispec', 'geojson'],
)
