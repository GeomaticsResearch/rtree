#!/usr/bin/env python
from setuptools import setup

import rtree

# Get text from README.txt
with open('docs/source/README.txt', 'r') as fp:
    readme_text = fp.read()

import os

if os.name == 'nt':
    if os.path.exists(r'C:\OSGeo4W64\bin\spatialindex_c-64.dll'):
        data_files = [('Lib/site-packages/rtree',
                  [r'C:\OSGeo4W64\bin\spatialindex_c-64.dll',
                   r'C:\OSGeo4W64\bin\spatialindex-64.dll'])]
    else:
        data_files = [('Lib/site-packages/rtree',
                  [r'C:\OSGeo4W64\bin\spatialindex_c.dll',
                   r'C:\OSGeo4W64\bin\spatialindex.dll'])]
else:
    data_files = None

setup(
    name          = 'Rtree',
    version       = rtree.__version__,
    description   = 'R-Tree spatial index for Python GIS',
    license       = 'LGPL',
    keywords      = 'gis spatial index r-tree',
    author        = 'Sean Gillies',
    author_email  = 'sean.gillies@gmail.com',
    maintainer        = 'Howard Butler',
    maintainer_email  = 'hobu@hobu.net',
    url   = 'http://toblerity.github.com/rtree/',
    long_description = readme_text,
    packages      = ['rtree'],
    install_requires = ['setuptools'],
    test_suite = 'tests.test_suite',
    data_files = data_files,
    zip_safe = False,
    classifiers   = [
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
      'Operating System :: OS Independent',
      'Programming Language :: C',
      'Programming Language :: C++',
      'Programming Language :: Python',
      'Topic :: Scientific/Engineering :: GIS',
      'Topic :: Database',
      ],
)
