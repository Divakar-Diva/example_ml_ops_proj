from setuptools import setup,find_packages
from typing import List
def get_requirements( file_path : str) -> List[str]:
    gb='-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements=[req.strip() for req in file_obj.readlines()]
        if gb in requirements:
            requirements.remove(gb)
    return requirements
setup(
     name="ML project",
    version="0.0.1",
    author="divakar",
    author_email="divakardiva498@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
