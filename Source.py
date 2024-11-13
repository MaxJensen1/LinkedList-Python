from typing import TypeVar, Generic, Optional
from List import List
import sys, time

sys.setrecursionlimit(15000) # To not cap out at the default recursion depth at 1000

def main():
    testRuns = 100
    totalTime = 0

    for i in range(testRuns):
        list = List()
        list.AddFromtextFile("C:\\Users\\max.jensen\\Desktop\\text.txt")

        startTime = time.time()
        list.MergeSort()
        endTime = time.time()

        deltaTime = endTime - startTime
        print("Sorted ", list.GetLength(), " words in ", deltaTime, " seconds")   
        totalTime = totalTime + deltaTime    

    print("Average time to sort: ", totalTime/testRuns) 
    

if __name__ == "__main__":
    main()