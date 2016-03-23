#!/usr/bin/python
#-*- coding: utf-8 -*-
import urllib
import sys
try:
    import xml.etree.cElementTree as etree
except ImportError:
    import xml.etree.ElementTree as etree
    

#import importlib
#importlib.reload(sys)
#sys.setdefaultencoding( "utf-8" )
#print(sys.getdefaultencoding())

context = urllib.urlopen('http://ws.qunar.com/holidayService.jcp?lane=上海-嘉峪关')
tree = etree.parse(context)
root = tree.getroot()


#for elem in tree.iter():
#    print (elem.tag, elem.attrib)



for node in root[0]:
    for child in node:
        for child_detail in child.attrib.keys():
            if child.attrib["type"] == "go" and int(child.attrib["price"])<1400:
                print (child_detail,child.attrib[child_detail])

                    
'''
for node in root[0]:
    if node.attrib["date"] == "2016-03-30":
        print("find it")
        for child in node:
            for child_detail in child.attrib.keys():
                if child.attrib["type"] == "go" and int(child.attrib["price"])<2600:
                    print (child_detail,child.attrib[child_detail])
'''
                    
