from setuptools import setup

setup(
    name='casparlibs',
    version='0.1.0',    
    description='A CasparCG connector library',
    url='https://github.com/ubsms/casparlibs',
    author='Richard Franks',
    author_email='richard@ubsms.org.uk',
    license='MIT',
    packages=['casparlibs'],
    install_requires=['amcp-pylib>=0.2.2'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Religion',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
    ],
)