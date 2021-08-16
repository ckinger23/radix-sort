'''
Homework 5: Radix Sort
Carter King
Dr. Sanders
CS 355 Advanced Algorithms
21 October 2018
Python 3
'''

import sys

'''
Function: parseNumFile(filename)
 This function takes a .txt file of numbers and creates an array with these numbers.
 parameters: filename - a string of the name of the file
 returns: list - an array holding the numbers
'''


def parseNumFile(filename):
    list = []
    infile = open(filename, 'r')  # read the file and add elements to list
    for line in infile:
        value = str(line).strip()
        list.append(value)
    return list

'''
Function: radixSort(list, numDigits, holder)
 This function takes in a list of numbers and recursively calls itself until all of the numbers are sorted using 
 radix sort
 parameters: list - a list of the numbers to be sorted
             numDigits - an integer of the maximum number of digits for a number in the list
             holder - equal to integer one to be able to access the last character element in the number strings
 returns: list - the sorted list of numbers after recursively calling itself
'''

def radixSort(list, numDigits, holder):
    digits = [[], [], [], [], [], [], [], [], [], []] #10 inner lists for 10 digit places
    newList = []
    specDig = numDigits - 1 #access proper amount of characters in the number strings
    if specDig < 0: #sort finished
        return list
    for num in list:
        try:
            number = int(num[-holder]) #access from end character backward
            digits[number].append(num)
        except IndexError:
            digits[0].append(num) #if a digits place doesn't exist for a num, add to end of 0's place
    for line in range(10):
        newList += digits[line] #place back into list to call radixSort on this "semi-sorted" list
    return radixSort(newList, numDigits - 1, holder + 1)




def main():
    # Show them the default len is 1 unless they put values on the command line
    print(len(sys.argv))
    if len(sys.argv) == 3:
        fileName = sys.argv[1]
        numDigits = sys.argv[2]
    else:
        fileName = input("What .txt file would you like to use? ")
        numDigits = int(input("What is the Max number of digits for a number in the file? "))
        listNums = parseNumFile(fileName)
        sortedList = radixSort(listNums, numDigits, 1) #1 to start at end of characters
        print(sortedList)


main()
