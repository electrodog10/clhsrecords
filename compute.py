#!/usr/bin/env python
#import libraries and files
from app import loadXML
import os
from app import display
from xml.etree import ElementTree
from flask_table import Table, Col

def compute(r,option):
    
    #import XML file
    file_name = 'records.xml'
    full_name = os.path.abspath(os.path.join('recordfiles', file_name))
    # get variables from html 
    print(r)
    htmlName = r
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
    #addedArrays = ""
    #while name[x] != "Empty":
     #addedArrays = addedArrays +(str(name[x])+ ", " + str(activity[x]) +", "+ str(record[x]) +", "+ str(num[x])+", "+ str(year[x])) + " "
        #x = x + 1
    #r = addedArrays.title()
    # Declare your table

    class ItemTable(Table):
        namecol = Col('Name')
        activitycol = Col('Activity')
        recordcol = Col('Record')
        numcol = Col('Number')
        yearcol = Col('Year')


    # Get some objects
    class Item(object):
        def __init__(self, namecol, activitycol, recordcol, numcol, yearcol):
            self.namecol = namecol
            self.activitycol = activitycol
            self.recordcol = recordcol
            self.numcol = numcol
            self.yearcol = yearcol
    x = 0
    items = []
    while name[x] != "Empty":
        items = items + [dict(namecol=str(name[x]),activitycol=str(activity[x]),recordcol=str(record[x]),yearcol=str(year[x]),numcol=str(num[x]))]
        x = x + 1
    # Populate the table
    table = ItemTable(items)
    return table

