from setuptools import setup, find_packages
import python_lib_for_me


setup(
    name='python-lib-for-me',
    version=python_lib_for_me.__version__,
    # description='',
    # long_description='',
    # url='',
    # author='',
    # author_email='',
    # license='',
    # classifiers='',
    # keywords='',
    # project_urls={},
    packages=find_packages(),
    install_requires=['python-dateutil'],
    python_requires='>=3.10',
)
