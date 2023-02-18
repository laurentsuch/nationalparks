# Lauren Tsuchiyama, ltsuchiy@usc.edu
# ITP 115, Spring 2022
# Section: 31881
# Final Project
# Description:
# This program produces a national parks library.
# tasks.py reads csv file, converts dates, and returns largest park in file.


# this function reads the national parks CSV file
# parameter is the file, which is national parks
# for some reason my computer named it national_parks(1) even though I did not download it before, but I just kept the name
# returns a list of dictionaries which represent each park (header of csv file are the keys)
def readParksFile(fileName="national_parks(1).csv"):
    parkList = []
    # empty list to hold dictionaries of parks
    fileIn = open(fileName, "r")
    # open file to read
    header = fileIn.readline()
    # skip the header line (header line is the keys of dictionaries)
    for line in fileIn:
        # loop through each line in the file - each line is a park
        line = line.strip()
        dataList = line.split(",")
        # strip lines and split lines using "," and store values in list
        park = {}
        # empty dictionary variable to hold park line
        code = dataList[0]
        # for each line, the first value in list is the code of the park  - store in variable
        name = dataList[1]
        # second element in each park list is name
        # repeat for rest of headers (state, acres, latitude..)
        state = dataList[2]
        acres = dataList[3]
        latitude = dataList[4]
        longitude = dataList[5]
        date = dataList[6]
        description = dataList[7:]
        # 7: to include the whole rest of description
        fullDescription = ""
        # string variable to hold full description
        fullDescription = fullDescription.join(description)
        # join together in variable for full description
        park["Code"] = code
        # park is now a dictionary - create key that is entitled "Code"
        # value is the corresponding element in line
        # continue for rest of header names, create keys and values from variables created
        park["Name"] = name
        park["State"] = state
        park["Acres"] = acres
        park["Latitude"] = latitude
        park["Longitude"] = longitude
        park["Date"] = date
        park["Description"] = fullDescription
        parkList.append(park)
        # because this is in for loop, we do this for each line (park)
        # add to parkList - list full of dictionaries of parks now
    fileIn.close()
    return parkList


# this function converts the date, which is separated by dashes into a date with month in words and in word format
# parameter is string to hold values of key["Date"] for each park
# no return value
def convertDate(dataStr):
    newDate = dataStr.split("-")
    # the value for key["Date"] is separated by "-"
    # use new variable to split parameter string variable with "-" into list
    year = newDate[0]
    month = int(newDate[1])
    day = newDate[2]
    # first element in list is year, second is month, third element in lsit is day
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    monthIndex = month - 1
    # because lists have indices that start with 0, index to find month in months list is month - 1
    monthWord = months[monthIndex]
    # locate month name using index
    print(monthWord, day + ",", year)


# this function gets the code of the largest park (acres) from the csv file
# parameter is the return value of readParks function; list of dictionaries of parks
# return value is code of largest park
def getLargestPark(parksList):
    acresList = []
    for park in parksList:
        acres = int(park["Acres"])
        # loop through each dictionary in list (park)
        # hold values of each park with key ["Acres"] in variable
        acresList.append(acres)
    acresList.sort()
    # sort numbers from smallest to biggest
    largest = acresList[len(acresList)-1]
    # largest park in acres is the last element in the list
    for park in parksList:
        if park["Acres"] == str(largest):
            return park["Code"]
    # to find code of park with largest number, use branching
    # if that value of Acres key == largest number, return value of that park's Code key


