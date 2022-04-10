from setuptools import setup, find_packages

setup(
    name='cmagick',
    version='0.1.0',
    author='Aissa Laribi',
    author_email='aissalaribi@yahoo.fr',
    description='An utility for converting and resizing images',
    long_description='README.md',
    long_description_content_type='text/x-rst',
    url='https://github.com/aissa-laribi/cmagick',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'cmagick=cmagick.main:main',
            ],
    }
    )
