from setuptools import setup, find_packages

setup(
    name='dac',
    version='0.1.0',
    description="Data-as-code",
    long_description="""\
        Decompose large datasets into data particles for rapid manipulation
        through configuration
    """,
    author='nickumia',
    packages=find_packages(include=['dac', 'dac.process'])
)
