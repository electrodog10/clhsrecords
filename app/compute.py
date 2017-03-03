#!/usr/bin/env python
#import libraries and files
from app import loadXML
import os
from app import display

def compute(r,option):
    #import XML file
    file_name = 'records.xml'
    full_name = os.path.abspath(os.path.join('recordfiles', file_name))
    # get variables from html
    htmlName = r
    htmlNumber = int(option)
    # initialize variables
    search = ['blank','name','activity','year','title']
    #searchnumber = ['1','2','3','4']
    searchXML = loadXML.searchingall(full_name) #finds all xml entries
    (name, activity, record, num, year) =  display.display(searchXML,htmlName,int(htmlNumber),search)
    #prep for arrays
    x = 0
    items = []
    while name[x] != "Empty":
        items.append(x)
        items[x] = [name[x],activity[x],record[x],num[x],year[x]]
        x = x + 1
    return items

