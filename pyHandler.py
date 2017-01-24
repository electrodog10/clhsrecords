#!/usr/bin/env python
#import libraries and files
import cgi, cgitb 
import os
import loadXML
import display
from xml.etree import ElementTree
#initalize getting info from the HTML
form = cgi.FieldStorage() # instantiate only once!
#import XML file
file_name = 'testrecords.xml' 
full_name = os.path.abspath(os.path.join('xml', file_name))
# get variables from html 

htmlName =  form.getfirst('name', 'empty')
htmlNumber = form.getvalue('searchcrit')

#htmlName = cgi.escape(htmlName)

# initialize variables
search = ['blank','name','activity','year','title']
searchnumber = ['1','2','3','4']

searchXML = loadXML.searchingall(full_name) #finds all xml entries
(name, activity, record, num, year) =  display.display(searchXML,htmlName,int(htmlNumber),search) 
#all vars coming out of the line above are arrays
x = 0
addedArrays = ["None"]
while name[x] != "Empty":
    addedArrays[x] = (str(name[x])+ "," + str(activity[x]) +","+ str(record[x]) +","+ str(num[x])+","+ str(year[x]))
    x = x + 1
    addedArrays.append(x)
#open html file
#with open('/test.html') as f:
#    htmlFile=(f.read())
#print("""\
#Content-Type: text/html\n 
#"#""+ htmlFile)# % htmlName)

print("""\
Content-Type: text/html\n
<html>
<body>
<p class="page-description">The returned items were "%s"</p>
</body>
</html>
""" % addedArrays)
