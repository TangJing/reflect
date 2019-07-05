#!/usr/bin/env python
#-*- coding:utf-8 -*-

import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()
setuptools.setup(
    name = "reflect",
    version = "1.0.0",
    keywords = ("pip", "reflect","featureextraction"),
    description = "An reflect class",
    long_description = long_description,
    long_description_content_typ="text/markdown",
    license = "MIT Licence",
    url = "https://github.com/TangJing/reflect",
    author = "T.D",
    author_email = "yeihizhi@163.com",
    packages = setuptools.find_packages(),
    classifiers=[]
)