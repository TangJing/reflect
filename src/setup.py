#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "reflect",      #这里是pip项目发布的名称
    version = "1.0.0",     #版本号，数值大的会优先被pip
    keywords = ("pip", "reflect","featureextraction"),
    description = "An reflect class",
    long_description = "An reflect class",
    license = "MIT Licence",

    url = "https://github.com/TangJing/reflect",     #项目相关文件地址
    author = "T.D",
    author_email = "yeihizhi@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []          #这个项目需要的第三方库
)