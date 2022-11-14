from setuptools import setup
from distutils.core import Extension

def get_extensions():
    return [Extension(name='my_package.include.hello_world',
                      sources=['src/my_package/include/hello_world.pyx'])]

setup(ext_modules=get_extensions())