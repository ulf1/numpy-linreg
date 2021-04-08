from setuptools import setup
import pypandoc


setup(name='numpy-linreg',
      version='0.1.0',
      description='Linear Regression with numpy only.',
      long_description=pypandoc.convert('README.md', 'rst'),
      url='http://github.com/ulf1/numpy-linreg',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['numpy_linreg'],
      install_requires=[
          'setuptools>=40.0.0',
          'numpy>=1.18.*',
          'numba>=0.48.*'],
      python_requires='>=3.6',
      zip_safe=False)
