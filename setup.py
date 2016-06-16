from distutils.core import setup
from setuptools import find_packages


setup(
    name='TensorGraph',
    version='1.0',
    author=u'Wu Zhen Zhou',
    author_email='hyciswu@gmail.com',
    install_requires=['numpy>=1.7.1', 'scipy>=0.11',
                      'six>=1.9.0', 'tensorflow>=0.8.0',
                      'scikit-learn>=0.17.1', 'pandas>=0.18.1'],
    url='https://github.com/hycis/TensorGraph',
    license='Apache licence, see LICENCE',
    description='A missing package of tensorflow for building all kinds of models',
    long_description=open('README.md').read(),
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True
)