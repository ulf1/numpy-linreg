from setuptools import setup
import os


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as fp:
        s = fp.read()
    return s


def get_version(path):
    with open(path, "r") as fp:
        lines = fp.read()
    for line in lines.split("\n"):
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setup(name='numpy-linreg',
      version=get_version("numpy_linreg/__init__.py"),
      description='Linear Regression with numpy only.',
      long_description=read('README.rst'),
      url='http://github.com/ulf1/numpy-linreg',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='Apache License 2.0',
      packages=['numpy_linreg'],
      install_requires=[
          'numpy>=1.18.*,<2',
          'numba>=0.48.*'],
      python_requires='>=3.6',
      zip_safe=True)
