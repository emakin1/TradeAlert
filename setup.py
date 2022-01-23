from setuptools import setup, find_packages
import os


setup(
    name='trade_alert',
    version='0.1',
    description='Stock inflection point alert system',
    author='Emma Baker',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'pandas-ta',
        'numpy',
        'matplotlib',
        'yfinance'
    ]
)