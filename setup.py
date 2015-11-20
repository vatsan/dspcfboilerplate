from setuptools import setup, find_packages

setup(
    name='dspcfboilerplate',
    author='Srivatsan Ramanujam <vatsan.cs@utexas.edu>',
    description='Boilerplate code for data science apps on PCF',
    version='0.1',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)
