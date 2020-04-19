from setuptools import setup

__version__ = '1.0.0'
__title__ = 'hcm_admin'
__author__ = 'Huawei'
__license__ = 'Apache License 2.0'
__url__ = 'https://developer.huawei.com/consumer/cn/'


REQUIRED = [
    'requests', 'six',
]

setup(
    name='huawei_pushkit',
    version='1.0.0',
    description='Huawei Pushkit Python SDK',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://developer.huawei.com/consumer/cn/',
    author='Huawei',
    license='Apache License 2.0',
    keywords='huawei cloud development',
    install_requires=REQUIRED,
    packages=['huawei_pushkit'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: Apache Software License',
    ],
)
