# -*- coding: utf-8 -*-
"""
Lawliet
-------------
you can response json like this "return {}"
"""
from setuptools import setup

setup(
    name='lawliet',
    version='2.1.1',
    description=u'这是一个给开源添乱的项目',
    author='Monomer Xu',
    author_email='fing@easymail.com.cn',
    url='https://github.com/fing520/Lawliet',
    py_modules=['lawliet'],
    packages=['lawliet'],
    license='MIT',
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
