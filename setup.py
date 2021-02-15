import setuptools


def get_long_description():
    with open('README.md', 'r') as file:
        return file.read()


def get_requirements():
    with open('requirements.txt') as file:
        return file.read().splitlines()


setuptools.setup(
    name='yf_api',
    version='0.1.0',
    author='Brennen Herbruck',
    author_email='brennen.hrbruck@gmail.com',
    description='Yahoo Finance API wrapper',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/bherbruck/yf-api-python',
    packages=['yf_api'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=get_requirements(),
    python_requires='>=3.6',
)
