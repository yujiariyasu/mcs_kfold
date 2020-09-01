# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='mcs_kfold',
    version='0.1.0',
    python_requires='==3.*,>=3.6.5',
    author='Masashi Sode',
    author_email='masashi.sode@gmail.com',
    license='MIT',
    packages=['mcs_kfold'],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'numpy==1.*,>=1.19.1', 'pandas==1.*,>=1.1.1',
        'scikit-learn==0.*,>=0.23.2', 'scipy==1.*,>=1.5.2'
    ],
    extras_require={
        "dev": [
            "autopep8==1.*,>=1.5.2", "black==19.*,>=19.10.0.b0",
            "flake8==3.*,>=3.8.2", "isort==4.*,>=4.3.21",
            "matplotlib==3.*,>=3.3.1", "mypy==0.*,>=0.770.0",
            "pytest==6.*,>=6.0.1"
        ]
    },
)