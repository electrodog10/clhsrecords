def display (searchXML,htmlName,htmlNumber,search):
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
    return(name, activity, record, num, year)