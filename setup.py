from setuptools import find_packages,setup



def get_req(file):
    with open('requirements.txt',mode='r') as data:
        req = data.readlines()
        req = [x.replace('\n',"") for x in req]
        if '-e .' in req:
             req.remove('-e .')
        return req


print(get_req('requirement.txt'))

setup(
     name="MLPROJECT",
     version="0.0.1",
     author='TheRugBRO',
     packages=find_packages(),
     install_requires=get_req('requirements.txt')
)