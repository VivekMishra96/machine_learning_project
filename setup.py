from setuptools import setup
from typing import List

#Declaring varibales for setup fucntions
PROJECT_NAME ="housing-predictor"
VERSION="0.0.1"
AUTHOR="Vivek Mishra"
DESCRIPTION="This is a first fsds Nov batch Machine learning"
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description:This fucntion is going to return list of requirements
    mention in requirements.txt file

    return This fucntion is going to return a list which contain name of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        return requirements_file.readlines()


setup(
name="PROJECT_NAME",
version="VERSION",
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()

)