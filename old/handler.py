import cgi
#import os
#import loadXML
#import display
#from xml.etree import ElementTree
form = cgi.FieldStorage() # instantiate only once!
#import file
#file_name = 'testrecords.xml' 
#full_name = os.path.abspath(os.path.join('xml', file_name))
# get variables from html 
htmlNumber = 1
name = form.getfirst('name', 'empty')

name = cgi.escape(name)

# initialize variables
#search = ['name','activity','year','record']
#searchnumber = ['1','2','3','4']

#searchXML = loadXML.searchingall(full_name) #finds all xml entries 
#(name, activity, record, num, year) =  display.display(searchXML,htmlName,int(htmlNumber),search) 
#all vars coming out of the line above are arrays

#pineapple = (name[0], activity[0], record[0], num[0], year[0])

print("""\
Content-Type: text/html\n
<html>
<p class="page-description">The submitted name was "%s"</p>
</body>
</html>
""" % name)
