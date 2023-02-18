# Lauren Tsuchiyama, ltsuchiy@usc.edu
# ITP 115, Spring 2022
# Section: 31881
# Final Project
# Description:
# This program produces a national parks library.
# main.py displays the program to the user.
import tasks
import interface


# this function displays menu to user, and displays choice to user
# no parameter
# no return value
def main():
    print("National Parks")
    forParksList = tasks.readParksFile(fileName="national_parks(1).csv")
    # variable for readParksFile to get return value (parksList)
    forMenuDict = interface.getMenuDict()
    # variable to hold menuDict variable
    interface.displayMenu(forMenuDict)
    # display menu
    forUserChoice = interface.getUserChoice(forMenuDict)
    # variable to hold user choice
    while forUserChoice.lower() != "q":
        # while loop, ends when user enters q or Q
        if forUserChoice.lower() == "a":
            interface.printAllParks(forParksList)
        elif forUserChoice.lower() == "b":
            interface.printParksInState(forParksList)
        elif forUserChoice.lower() == "c":
            interface.printLargestPark(forParksList)
        elif forUserChoice.lower() == "d":
            interface.printParksForSearch(forParksList)
        elif forUserChoice.lower() == "e":
            interface.printOldestPark(forParksList)
        elif forUserChoice.lower() == "f":
            interface.printStateMostParks(forParksList)
        # call functions according to branching and menu
        print()
        interface.displayMenu(forMenuDict)
        forUserChoice = interface.getUserChoice(forMenuDict)
        # display menu and choice input each time until user quits


main()
# call main function
