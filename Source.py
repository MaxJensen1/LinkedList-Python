from typing import TypeVar, Generic, Optional
from List import List
import sys, time
import os

sys.setrecursionlimit(15000) # To not cap out at the default recursion depth at 1000

def main():
    testRuns = 10
    totalTime = 0

    computerName = os.getlogin()
    fileLocation = f"C:\\Users\\{computerName}\\Desktop\\text.txt"

    for i in range(testRuns):
        list = List()
        list.AddFromtextFile(fileLocation)

        startTime = time.time()
        list.MergeSort()
        endTime = time.time()

        #list.PrintAll()

        deltaTime = endTime - startTime
        print("Sorted ", list.GetLength(), " words in ", deltaTime, " seconds")   
        totalTime = totalTime + deltaTime    

    print("Average time to sort: ", totalTime/testRuns) 
    

if __name__ == "__main__":
    main()