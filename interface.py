# Lauren Tsuchiyama, ltsuchiy@usc.edu
# ITP 115, Spring 2022
# Section: 31881
# Final Project
# Description:
# This program produces a national parks library.
# interface.py defines functions that help user run the program.
import tasks


# this function creates a dictionary for the menu to display to user
# no parameter
# return value is the dictionary created - keys are options and values are string values correspond to each choice
def getMenuDict():
    menuDict = {}
    menuDict["A"] = "All national parks"
    menuDict["B"] = "Parks in a particular state"
    menuDict["C"] = "The largest park"
    menuDict["D"] = "Search for a park"
    menuDict["E"] = "The oldest park"
    menuDict["F"] = "State with most parks"
    menuDict["Q"] = "Quit"
    # creating dictionary by adding keys and values (strings)
    return menuDict


# this function displays the menu to the user
# the parameter is dictionary of menu that was returned above
# no return valeu
def displayMenu(menuDict):
    for key in menuDict:
        print(key, "-->", menuDict[key])
    # for each key in menuDict (from previous function), print its value to display menu


# this function gets use choice from menu selection
# parameter is dictionary of menu from getMenuDict function
# return value is the letter user chooses in upper case (to match keys)
def getUserChoice(menuDict):
    userChoice = input("Choice: ")
    while userChoice.upper() not in menuDict.keys():
        userChoice = input("Choice: ")
    # continue to ask for choice until user enters a key element from menuDict
    return userChoice


# I created this function to clean up some code
# parameters is dictionary object, specifically certain keys of park dicts whose values need to be located
# park parameter represents the dictionary name
# prints value of certain key
# no return value
def printKeyPark(dictObject, park):
    park[dictObject] = park.get(dictObject)
    # get value of key (dictObject)
    print(park[dictObject])


# I created this function to clean up some code
# this function prints code out in correct format so don't have to copy/repeat whole block of code
# parameter is dictionary name (park)
# function is essentially just to print out parks in correct format and clean up other following functions
# did not include description key here because "printAllParks" does not need description of park
# added description of park when necessary to individual functions
def printParkDesc(dictName):
    name = dictName["Name"]
    printCode = dictName["Code"]
    print(name, "(" + printCode + ")")
    print("\tLocation: ", end="")
    printKeyPark("State", dictName)
    # call function above to get value of key["State"]
    print("\tArea: ", end="")
    dictName["Acres"] = dictName.get("Acres")
    print(dictName["Acres"], "acres")
    print("\tDate established: ", end="")
    tasks.convertDate(dataStr=dictName["Date"])
    # to convert date, parameter is the value of Date key for each park


# function prints all parks in correct format
# parameter is parksList return in tasks.py readParksFile
# no return value
def printAllParks(parksList):
    for park in parksList:
        printParkDesc(park)
    # to print all parks , call function above to print in correct format
    # all parks = loop through each dictionary in parksList


# this function gets state abbreviation user wants to search for parks in
# no parameter
# return value is user inputted state in upper case
def getStateAbbr():
    userState = input("Enter a state: ")
    while len(userState) != 2:
        # ensure that user enters a two letter input
        print("Need the two letter abbreviation")
        userState = input("Enter a state: ")
    return userState.upper()


# this function prints all parks from the state user chooses
# parameter is returned value from tasks.py readParksFile
# no return value
def printParksInState(parksList):
    stateName = getStateAbbr()
    counter = 0
    # hold counter in order to initiate code for when state does not exist or not in values of each park dict
    for park in parksList:
        if park["State"] == stateName:
            counter = counter + 1
            printParkDesc(park)
            # if state is a value in "State" key, print that park
            # increase count
    if counter == 0:
        print("There are no national parks in " + stateName + " or it is not a valid state.")
        # if count remains 0, print statement above


# this function prints the largest park from csv file using tasks.getLargestPark
# parameter is returned value from tasks.py readParksFile
# no return value
def printLargestPark(parksList):
    largestPark = tasks.getLargestPark(parksList)
    # hold variable for function in tasks.py that returns code for largest park
    for park in parksList:
        if park["Code"] == largestPark:
            # locate park that has that code
            printParkDesc(park)
            print("\tDescription: ", end="")
            printKeyPark("Description", park)
            # print function along with other descriptors


# this function prints all parks that include search word user inputs
# parameter is returned value from tasks.py readParksFile
# no return value
def printParksForSearch(parksList):
    userSearch = input("Enter text for searching: ")
    counter = 0
    # similar to above, hold counter to dictate when word for search does not appear in parksList
    for park in parksList:
        if userSearch in park["Code"] or userSearch in park["Name"] or userSearch in park["Description"]:
            # if word is in any of the park values from above keys, print park and increase counter
            counter = counter + 1
            # increase count if word is detected in a park
            printParkDesc(park)
            print("\tDescription: ", end="")
            printKeyPark("Description", park)
    if counter == 0:
        print("There are no national parks for the search text " + "'" + userSearch + "'.")
        # if word not in any dictionaries in parksList, print above statement


# this function prints the oldest park
# parameter is returned value from tasks.py readParksFile
# no return value
def printOldestPark(parksList):
    dateList = []
    for park in parksList:
        dates = park["Date"]
        dateList.append(dates)
        # hold all date values of all parks using "Date" key in list (dateList)
        dateList.sort()
        # sort from year - first index is oldest park
        oldest = dateList[0]
    for park in parksList:
        if park["Date"] == oldest:
            printParkDesc(park)
            print("\tDescription: ", end="")
            printKeyPark("Description", park)
        # locate the park that has that date using key

# this function prints all the parks from the state that has the most parks
# parameter is returned value from tasks.py readParksFile
# no return value
def printStateMostParks(parksList):
    stateList = []
    for park in parksList:
        states = park["State"]
        stateList.append(states)
    # similar to above, put all states in a list
    max = 0
    # max variable set to 0 in order to compare the frequency number
    abbreviation = stateList[0]
    # abbreviation variable is set to first value because if we did not have this variable, it would just return all states who have more parks than max
    # create variables to find max frequency of state
    for j in stateList:
        # loop through each value in list
        freq = stateList.count(j)
        # count how many times each element occurs in list
        if freq > max:
            # to find max, compare to max variable
            max = freq
            # assign variable to max
            abbreviation = j
            # find state abbreviation
    print("The state with the most parks is " + abbreviation)
    for park in parksList:
        if park["State"] == abbreviation:
            printParkDesc(park)
            print("\tDescription: ", end="")
            printKeyPark("Description", park)









