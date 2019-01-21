from setuptools import setup, find_packages

with open('README.md') as fp:
    long_description = fp.read()

setup(
    name='discussion-bot',
    version='0.0.1',
    author='Armon Rabiyan',
    author_email='armon@wikia-inc.com',
    packages=find_packages(),
    scripts=[],
    url='http://github.com/armonr/discussion-bot',
    license='LICENSE',
    description='A conversation emulator bot for Wikia discussion service',
    long_description=long_description,
    install_requires=[
        'Flask==1.0.2',
        'PyYAML==4.2b1',
        'requests==2.20.0',
        'cobe==2.1.2'
    ],
    include_package_data=True,
)
