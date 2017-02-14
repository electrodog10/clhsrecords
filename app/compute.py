#!/usr/bin/env python
#import libraries and files
from app import loadXML
import os
from app import display
from xml.etree import ElementTree

def compute(r,option):
    
    #import XML file
    file_name = 'testrecords.xml' 
    full_name = os.path.abspath(os.path.join('app','xml', file_name))
    # get variables from html 
    print(r)
    htmlName = r.lower()
    print(htmlName)
    htmlNumber = int(option)



    # initialize variables
    search = ['blank','name','activity','year','title']
    searchnumber = ['1','2','3','4']

    searchXML = loadXML.searchingall(full_name) #finds all xml entries
    (name, activity, record, num, year) =  display.display(searchXML,htmlName,int(htmlNumber),search) 
    print(name, activity, record, num, year) 
    #all vars coming out of the line above are arrays
    x = 0
    addedArrays = ""
    while name[x] != "Empty":
        addedArrays = addedArrays +'<br>'+(str(name[x])+ "," + str(activity[x]) +","+ str(record[x]) +","+ str(num[x])+","+ str(year[x]))+'<br>'
        x = x + 1
    r = addedArrays
    print(r)
    return r

