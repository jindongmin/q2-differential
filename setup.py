from setuptools import find_packages, setup
from glob import glob

classes = """
    Development Status :: 3 - Alpha
    License :: OSI Approved :: BSD License
    Topic :: Software Development :: Libraries
    Topic :: Scientific/Engineering
    Topic :: Scientific/Engineering :: Bio-Informatics
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3 :: Only
    Programming Language :: Python :: 3.4
    Programming Language :: Python :: 3.5
    Programming Language :: Python :: 3.6
    Programming Language :: Python :: 3.7
    Operating System :: Unix
    Operating System :: POSIX
    Operating System :: MacOS :: MacOS X
"""
classifiers = [s.strip() for s in classes.split('\n') if s]

description = ('QIIME2 plugin for '
               'Differential Abundance Analysis.')


setup(name='q2-differential',
      version='0.1.0',
      license='BSD-3-Clause',
      description=description,
      author_email="jamietmorton@gmail.com",
      maintainer_email="jamietmorton@gmail.com",
      packages=find_packages(),
      install_requires=[
          'numpy',
          'scipy',
          'pandas',
          'xarray',
          'arviz',
          'matplotlib',
          'cmdstanpy'
      ],
      entry_points={
          'qiime2.plugins': ['q2-differential=q2_differential.plugin_setup:plugin']
      },
      package_data={
          "q2_differential": ['assets/*'],
      },
      scripts=glob('scripts/*.py'),
      classifiers=classifiers)
