from setuptools import find_packages
from setuptools import setup

setup(
	name='weird, not-weird',
	version='1.0.0',
	desription='this program checks if a function is weird or not',
	author='Sahil Rajesh Nande',
	author_email='snande@ncsu.edu',
	url='https://github.com/shantanu109/Group_28_SE_Group/blob/main/code/program.py',
	install_requires=[],
	packages=find_packages(),
	long_description="""\
		Module for checking if a number is weird or not.

		Rules for weird:
		*A number is weird if n is odd
		*A number is weird if n is even and in the range[6,20]
		*A number is not weird if n is even and in the range[2,5]
		*A number is not weird if n is even and is greater than 20
		"""
	
)
