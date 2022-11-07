from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='cmagick',
    version='0.1.4',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    author='Aissa Laribi',
    author_email='aissalaribi@yahoo.fr',
    description='An utility for converting and resizing images',
    url='https://github.com/aissa-laribi/cmagick',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'cmagick=cmagick.main:main',
            ],
    }
    )
