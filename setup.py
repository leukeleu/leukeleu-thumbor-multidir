# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='thumbor_multidir',
    version='0.2.1',
    description="Thumbor file loader for multiple paths",
    long_description="""
Allows Thumbor to load files from multiple paths.

Checks a list of paths for exsitance of file prior to loading it.
""",
    keywords='imaging face detection feature thumbor file loader',
    author='Benn Eichhorn',
    author_email='beichhor@gmail.com',
    url='https://github.com/benneic/thumbor_multidir',
    license='MIT',
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Natural Language :: English',
                 'Operating System :: MacOS',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                 'Topic :: Multimedia :: Graphics :: Presentation'],
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'python-dateutil',
        'thumbor>=6.0.0,<7',
    ],
    extras_require={
    },
)