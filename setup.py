from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name = 'abnamro',
    version = '0.0.1',
    description = 'Python test',
    long_description = readme(),
    long_description_content_type = 'text/markdown',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    author = 'Mudit Mittal',
    author_email = 'muditmittal2007@gmail.com',
    keywords = 'core package',
    license = 'MIT',
    packages = ['txt2csv'],
    install_requires = [],
    include_package_data = True,
    zip_safe = False
)