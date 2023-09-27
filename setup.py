from setuptools import setup, find_packages

setup(
    name='fixerio-client',
    version='0.1.0',
    description='A Python client for the fixer.io foreign exchange API.',
    long_description='A library of clients for the fixer.io foreign exchange API. It includes clients for each tier '
                     'of subscription from Free to Professional Plus. This library is an extended adaption of fixerio '
                     'by amatellanes (https://github.com/amatellanes/fixerio)',
    author='Isaac',
    url='https://github.com/isaaclm/fixerio-client',
    license='MIT License',
    packages=['fixerio'],
    package_dir={'fixerio': 'fixerio'},
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)