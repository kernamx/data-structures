"""."""
from setuptools import setup

setup(

    name='data-structures',
    description='Data Structures Implementation',
    package_dir={'': 'src'},
    author='Robert Bronson',
    author_email='',
    py_modules=['linked_list'],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'tox'],
        'development': ['ipython']
    },
    entry_points={}

)
