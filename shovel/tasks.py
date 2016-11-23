import os
from shovel import task

VENV = './venv/bin/'
REQUIREMENTS = 'requirements.txt'
PACKAGE_NAME = '_'

@task
def install():
    print('Install latest dependencies')
    os.system('{}pip install -r {}'.format(VENV, REQUIREMENTS))


@task
def test():
    print('walker')
    os.system('{}nosetests test'.format(VENV))

@task
def testone(testfile):
    print('alejandro')
    os.system('{}nosetests test/{}'.format(VENV, testfile))
