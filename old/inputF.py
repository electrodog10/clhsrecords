def inputFunc ():
    userInput = input()
    return(userInput)

def inputFuncValidation (userInput):
    if userInput == '1' or userInput == '2' or userInput == '3' or userInput == '4' :
        valid = userInput
    else:
        valid = 0
    return(valid)