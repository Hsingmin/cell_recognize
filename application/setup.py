
# setup.py

from setuptools import setup, find_packages
 
setup(name='cell-detect',
      version='0.1',
      url='https://github.com/Hsingmin/cell_recognize',
      license='The Unlicense',
      author='Hsingmin Lee',
      author_email='leehsingmin@gmail.com',
      description='Distribute as a package',
      packages=find_packages(),
      # long_description=open('README.md').read(),
      zip_safe=False)
