import sys

try:
    from setuptools import setup
    from setuptools.extension import Extension
except ImportError:
    print("Couldn't import setuptools. Falling back to distutils.")
    from distutils.core import setup

try:
    from Cython.Distutils import build_ext
except ImportError:
    print("Could not import Cython.Distutils. Install `cython` and rerun.")
    sys.exit(1)

ext_modules = [Extension("hello", ["hello.pyx"])]

setup(
  name = 'Hello world app',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules,
  install_requires = ['Cython'],
  test_suite='test',
)
