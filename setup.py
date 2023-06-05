""" This folder help to create project as package and deploy in pypi"""


from setuptools import find_packages,setup



setup(name = 'mlproject',
      version = '0.0.1',
      author = 'balaji',
      author_email = 'balajiharidasan@gmail.com',
      packages=find_packages(),  # this line will see where there is the __init__ and install it
      install_requires = ['pandas','numpy','seaborn'])

