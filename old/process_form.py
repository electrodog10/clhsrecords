#import cgi
 #import os
 #import loadXML
 #import display
 #from xml.etree import ElementTree
#form = cgi.FieldStorage() # instantiate only once!
#import file
 #file_name = 'testrecords.xml' 
 #full_name = os.path.abspath(os.path.join('xml', file_name))
# get variables from html 
 #htmlNumber = 1
#name = form.getfirst('name', 'empty')

#name = cgi.escape(name)

# initialize variables
 #search = ['name','activity','year','record']
 #searchnumber = ['1','2','3','4']

 #searchXML = loadXML.searchingall(full_name) #finds all xml entries 
 #(name, activity, record, num, year) =  display.display(searchXML,htmlName,int(htmlNumber),search) 
#all vars coming out of the line above are arrays

 #addedArrays = (str(name[0]), str(activity[0]), str(record[0]), str(num[0]), str(year[0]))


#print("""\
#Content-Type: text/html\n
#<html>
#<p class="page-description">The submitted name was "%s"</p>
#</body>
#</html>
#""" % name)

#!/usr/bin/env python
import cgi
form = cgi.FieldStorage() # instantiate only once!
name = form.getfirst('name', 'empty')

# Avoid script injection escaping the user input
name = cgi.escape(name)

print("""\
Content-Type: text/html\n
<html><body>
<p>The submitted name was "%s"</p>
</body></html>
""" % name)

