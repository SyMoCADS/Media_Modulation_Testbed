from setuptools import setup, find_packages
import os

setup(
    name='mmtb',
    version='0.1.0',
    author='Lukas Brand, Maike Scherer, Louis Wolf',
    author_email='lukas.brand@fau.de, maike.scherer@fau.de, louis.wolf@fau.de',
    description='Code for the evaluation of data from the media modulation testbed.',
    license="MIT",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SyMoCADS/Media_Modulation_Testbed.git',
    packages=find_packages(),
    package_data={"mmtb.evaluation": ["*.json"], "mmtb.experiments": ["*.db", "*.json", "*.png"]},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
    install_requires=["statsmodels>=0.14.4",
                      "matplotlib>=3.9.2",
                      "numpy>=2.1.2",
                      "polars>=1.9.0",
                      "pydantic>=2.9.2",
                      "pydantic_core>=2.23.4"],
)
