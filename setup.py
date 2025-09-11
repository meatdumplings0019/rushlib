from setuptools import setup, find_packages

setup(
    name='rushlib',
    version='0.1.0',
    packages=find_packages(),
    requires=[
        'colorama'
    ],
    description='python lib',
    author='ndrzy',
    python_requires='>=3.10'
)