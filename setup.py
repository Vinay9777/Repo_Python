from setuptools import setup, find_packages

setup(
    name='tic_tac_toe',
    version='0.1.0',
    packages=find_packages(),
    author='Vinay Kumar Dubba',
    description='A simple Python Tic Tac Toe game',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
