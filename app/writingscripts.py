def createXML (nametext,activitytext,titletext,yeartext,numvaluetext) :
    #things that need to be imported
    from xml.etree.ElementTree import Element
    import xml.etree.ElementTree as etree
    from app import indent
    import os.path
    idvalue = 0
    #checking for  files
    pathofxml = os.path.abspath(os.path.join('recordfiles', 'records.xml'))
    pathofnum = os.path.abspath(os.path.join('recordfiles', 'num.txt'))
    xmlfileexist = os.path.exists(pathofxml)
    numfileexist = os.path.exists(pathofnum)
    #defining vars
    record = Element('record')
    name = Element('name')
    activity = Element('activity')
    title = Element('title')
    numvalue = Element('numvalue')
    year = Element('year')
    idnum = Element('idnum')
    #main for num.txt
    if numfileexist == 0:
        with open(pathofnum, 'w') as x:
            x.write('0')
    else:
        idvalue = open(pathofnum, 'r').read()
    #main part for creating xml
    if xmlfileexist == 0 :
        root = Element('school_records')
        tree = Element(root)
    else:
        tree = etree.parse(pathofxml)
        root = tree.getroot()
    #tag with info
    root.append(record)
    record.append(name)
    name.text = nametext
    record.append(activity)
    activity.text = activitytext
    record.append(title)
    title.text = titletext
    record.append(year)
    year.text = yeartext
    record.append(numvalue)
    numvalue.text = numvaluetext
    record.append(idnum)
    idnum.text = idvalue
    indent.indent(root)  #styling
    idvalue = int(idvalue) + 1 #adding to id number
    #wrting
    with open(pathofxml, 'wb') as f: #writes xml data
        f.write(etree.tostring(root))
    os.remove(pathofnum)
    with open(pathofnum, 'w') as f: #writes number data
        f.write(str(idvalue))
    return()

def deleteXML (deletionnum):
    #defining var, importing, and checking
    import xml.etree.ElementTree as etree
    import os.path
    pathofxml = "records.xml"
    xmlfileexist = os.path.exists(pathofxml)
    #checks for file
    if xmlfileexist == 1:
        tree = etree.parse(pathofxml)
        root = tree.getroot()
    else:
        return()
    #deletion process
    for country in root.findall('record'):
        idnum = country.find('idnum').text
        if idnum == deletionnum:
            root.remove(country)
        else:
            print("No Match")
        tree.write(pathofxml)
    return()