# SORT ANALYZER STARTER CODE

import time


#Initialize a function that will use bubble sort 
def bubbleSort(anArray):
    for numCompare in range(len(anArray)-1, 0, -1):
        for i in range(numCompare):
            if anArray[i] > anArray[i + 1]:
                temp = anArray[i]
                anArray[i] = anArray[i + 1]
                anArray[i + 1] = temp


#Initliaze a function that will use selection sort 
def selectionSort(anArray):
    for fillSlot in range(0, len(anArray)-1):
        #Search for minimum
        minPosition = fillSlot
        for i in range(fillSlot +1 , len(anArray)):
            if anArray[i] < anArray[minPosition]:
                minPosition = i
       
        temp = anArray[fillSlot]
        anArray[fillSlot] = anArray[minPosition]
        anArray[minPosition] = temp


#Initliaze a function that uses insertion sort 
def insertionSort(anArray):
    for i in range(1, len(anArray)):
        insertVal = anArray[i]
        insertPos = i

        while insertPos > 0 and anArray[insertPos - 1] > insertVal:
            anArray[insertPos] = anArray[insertPos-1]
            insertPos-=1

        anArray[insertPos] = insertVal


#Initialize a function that will time each sort algorithm
def sortTimer(searchFunction, array, arrayName, functionName):
    startTime = time.perf_counter()
    searchFunction(array)
    endTime = time.perf_counter()
    print(arrayName + " took " + str(endTime - startTime) + " seconds in " + functionName)


# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")


#Call the functions
sortTimer(bubbleSort, randomData, "randomData", "bubbleSort")
sortTimer(selectionSort, randomData, "randomData", "selectionSort")
sortTimer(insertionSort, randomData, "randomData", "insertionSort")

sortTimer(bubbleSort, reversedData, "reversedData", "bubbleSort")
sortTimer(selectionSort, reversedData, "reversedData", "selectionSort")
sortTimer(insertionSort, reversedData, "reversedData", "insertionSort")

sortTimer(bubbleSort, nearlySortedData, "nearlySortedData", "bubbleSort")
sortTimer(selectionSort, nearlySortedData, "nearlySortedData", "selectionSort")
sortTimer(insertionSort, nearlySortedData, "nearlySortedData", "insertionSort")

sortTimer(bubbleSort, fewUniqueData, "fewUniqueData", "bubbleSort")
sortTimer(selectionSort, fewUniqueData, "fewUniqueData", "selectionSort")
sortTimer(insertionSort, fewUniqueData, "fewUniqueData", "insertionSort")

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
# print(randomData[0:50])
# print(reversedData[0:50])
# print(nearlySortedData[0:50])
# print(fewUniqueData[0:50])

