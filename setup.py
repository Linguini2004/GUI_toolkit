import os, sys
from distutils.core import setup, Extension

packages = ['Widgets', 'Resources', 'Layouts']

version = "0.1"

if __name__ == '__main__':
  setup(
      name='GUIToolkit',
      version=version,
      url='https://github.com/Linguini2004/GUI_toolkit',
      license='LICENSE.txt',
      author='Davide Masini',
      author_email='davide.masini@example.com',
      description='GUI Toolkit',
      long_description=open("README.md").read(),
      classifiers=[],
      install_requires=["pygame"],
      packages=packages,
  )
