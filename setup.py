#from this file anybody can install this project and use it.

from setuptools import find_packages, setup  #This will automatically find the package that are available in the entire application 
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()                              #requirements.txt k har line ko read kara rahe hai
        requirements = [req.replace('\n','') for req in requirements]    #hamara jo requirements.txt file hai usme ka \n na aye bolke hum replace karre hai

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
#metadata information of the entire project
setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Sanjana',
    author_email = 'sanjana.sao01@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)