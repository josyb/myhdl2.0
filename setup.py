""" myhdl2's distribution and installation script. """

import ast
import fnmatch
import re
import os
import sys

from collections import defaultdict

if sys.version_info < (3, 11):
    raise RuntimeError("Python version 3.11+ required.")


# Prefer setuptools over distutils
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('myhdl2/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

data_root = 'share/myhdl2'
cosim_data = defaultdict(list)
for base, dir, files in os.walk('cosimulation'):
    for pat in ('*.c', 'Makefile*', '*.py', '*.v', '*.txt'):
        good = fnmatch.filter(files, pat)
        if good:
            cosim_data[base].extend(os.path.join(base, f) for f in good)

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="myhdl2",
    version=version,
    description="Python as a Hardware Description Language",
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author="Josy Boelen",
    author_email="josyboelen@gmail.com",
    url="http://www.myhdl.org",
    packages=['myhdl2', 'myhdl2.conversion'],
    data_files=[(os.path.join(data_root, k), v) for k, v in cosim_data.items()],
    license="LGPL",
    platforms='any',
    keywords="HDL ASIC FPGA hardware design",
    python_requires='>=3.11',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
    ]
)
