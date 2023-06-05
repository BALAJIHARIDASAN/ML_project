""" This folder help to create project as package and deploy in pypi"""


from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->list[str]:
    reqirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.repleace('\n',"") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(name = 'mlproject',
      version = '0.0.1',
      author = 'balaji',
      author_email = 'balajiharidasan@gmail.com',
      packages=find_packages(),  # this line will see where there is the __init__ and install it
      install_requires = get_requirements('requirements.txt'))

