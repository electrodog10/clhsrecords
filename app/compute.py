import os
from xml.etree import ElementTree


file_name = 'testrecords.xml'
full_name = os.path.abspath(os.path.join('app','xml', file_name))




def compute(r):
    
    htmlName = r # form.getfirst('name', 'empty')
    htmlNumber = 3  # form.getvalue('searchcrit')
    

    # initialize variables
    search = ['blank', 'name', 'activity', 'year', 'title']
    searchnumber = ['0','1', '2', '3', '4']

    def searchingall(filename):
        doc = ElementTree.parse(filename)
        records = doc.findall('record')
        return (records)

    def display(searchXML, htmlName, htmlNumber, search):
        displaycounter = -1
        name = ['None']
        activity = ['None']
        record = ['None']
        num = ['None']
        year = ['None']

        for x in searchXML:
            if htmlName == (x.find(search[int(htmlNumber)]).text):
                displaycounter = int(displaycounter) + 1
                name.append(displaycounter)
                activity.append(displaycounter)
                record.append(displaycounter)
                num.append(displaycounter)
                year.append(displaycounter)
                name[displaycounter] = x.find('name').text
                activity[displaycounter] = x.find('activity').text
                record[displaycounter] = x.find('title').text
                num[displaycounter] = x.find('numvalue').text
                year[displaycounter] = x.find('year').text
        displaycounter = displaycounter + 1
        name[displaycounter] = "Empty"
        return (name, activity, record, num, year)

    searchXML = searchingall(full_name)  # finds all xml entries
    (name, activity, record, num, year) = display(searchXML, htmlName, int(htmlNumber), search)
    print(name, activity, record, num, year)
    # all vars coming out of the line above are arrays
    x = 0
    addedArrays = ["None"]
    while name[x] != "Empty":
        addedArrays[x] = (
        str(name[x]) + "," + str(activity[x]) + "," + str(record[x]) + "," + str(num[x]) + "," + str(year[x]))
        x = x + 1
        addedArrays.append(x)
    arrayString = str(addedArrays)
    output = arrayString.title()
    
    return output

