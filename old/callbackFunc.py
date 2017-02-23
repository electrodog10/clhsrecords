# calling back the selection using userInput variable
def callback (userInput,searchnumber,search):
    callstr = 'none'
    if userInput == searchnumber[0]:
        callstr = search[0]
    if userInput == searchnumber[1]:
        callstr = search[1]
    if userInput == searchnumber[2]:
        callstr = search[2]
    if userInput == searchnumber[3]:
        callstr = search[3]
    return(callstr)