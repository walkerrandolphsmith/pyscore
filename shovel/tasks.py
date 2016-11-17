import os
from shovel import task

VENV = './venv/bin/'
REQUIREMENTS = 'requirements.txt'
PACKAGE_NAME = '_'

@task
def install():
    print('Install latest dependencies')
    os.system('{0}pip install -r {1}'.format(VENV, REQUIREMENTS))


@task
def test():
    print('walker')
    os.system('{0}nosetests test'.format(VENV))