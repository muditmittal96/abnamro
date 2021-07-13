from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='abnamro',
    version='0.0.1',
    description='',
    license='MIT',
    long_description=long_description,
    long_description_context_type='',
    packages=find_packages(where='src'),
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3.9",
    ]
)