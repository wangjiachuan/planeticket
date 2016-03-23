#!/usr/bin/python
#-*- coding: utf-8 -*-
#coding=gbk
import xml.etree.ElementTree as etree
import urllib
import sys
#import importlib
#importlib.reload(sys)
#sys.setdefaultencoding( "utf-8" )
print(sys.getdefaultencoding())

context = urllib.urlopen('http://ws.qunar.com/holidayService.jcp?lane=上海-嘉峪关')
tree = etree.parse(context)
root = tree.getroot()
for node in root[0]:
    if node.attrib["date"] == "2016-03-30":
        for child in node:
            for child_detail in child.attrib.keys():
                if child.attrib["type"] == "go" and int(child.attrib["price"])<600:
                    print (child_detail,child.attrib[child_detail])
                    
