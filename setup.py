from setuptools import setup, find_packages

setup(
    name='cmagick',
    version='0.0.1',
    author='Aissa Laribi',
    author_email='aissalaribi@yahoo.fr',
    description= 'An utility for converting and resizing images',
    url='https://github.com/aissa-laribi/cmagick',
    packages=find_packages('src'),
    package_dir={'':'src'},
    entry_points={
        'console_scripts': [
            'cmagick=cmagick.main:main',
            ],
    }
    )
