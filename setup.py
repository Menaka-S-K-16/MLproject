from setuptools import find_packages, setup
from typing import List

setup_connection_value = "-e ."
#collect all requirements from requirements.txt one by one and return a list with strings
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        #by default \n will be inserted in the list requirements from the .txt file and replace() is used to replace \n as ''
        # i.e) list comprehension
        requirements = [req.replace("\n","") for req in requirements]

        #to ignore -e . from requirements.txt which links the setup.py with requirements.txt
        if setup_connection_value in requirements:
            requirements.remove(setup_connection_value)
    return requirements
setup(

    name='end-to-end ML Project',
    version='0.0.1',
    author='Menaka',
    author_email='menakask16011998@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)