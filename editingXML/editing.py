import writingscripts #also dependent on the indent.py, must be in the same folder
#comment
write = int(input("Type 1 for Write, Type 2 for Delete"))



if write == 1:
    namefield = input(print('Name:'))
    activityfield = input(print('Activity:'))
    titlefield = input(print('Title:'))
    yearfield = input(print('Year:'))
    numvaluefield = input(print('Number Value:'))
    writingscripts.createXML(namefield, activityfield, titlefield, yearfield, numvaluefield)
if write == 2:
    idnumfield = input(print('id Number for Deletion:'))
    writingscripts.deleteXML(idnumfield)

print('done!')