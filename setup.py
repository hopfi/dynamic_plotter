from setuptools import setup, find_packages

setup(
    name='dynamic_plotter',
    version='0.0.1',
    packages=find_packages(include=['dyn_ploter', 'dyn_ploter.*'])
)