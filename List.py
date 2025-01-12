from typing import TypeVar, Generic, Optional
from Node import Node

T = TypeVar('T')

class List(Generic[T]):
    # You need to do this kind of initializing to be able to access variables
    def __init__(self):
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self.listLength = 0
        self.bannedCharacters = {',', '.', '(', ')', '"', ';', ':'}


    def MergeSort(self): # Need to include self to access variables
        self.head = self.StartMergeSort(self.head)


    def StartMergeSort(self, head: Node):
        # Can't sort an empty list
        if head is None or head.next is None:
            return head
        
        secondHalf: Node = self.SplitListInHalf(head)
        head = self.StartMergeSort(head)
        secondHalf = self.StartMergeSort(secondHalf)

        return self.Merge(head, secondHalf)


    def SplitListInHalf(self, head: Node):   
        #Can't split empty list or if there's only one node
        if head is None or head.next is None:
            return None
        
        slowPointer: Node = head
        fastPointer: Node = head.next

        # Find the middle of the list by finding the end, and moving the slow point half as much as the fast one.
        while fastPointer is not None and fastPointer.next is not None:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next

        secondHalf: Node = slowPointer.next
        slowPointer.next = None

        return secondHalf


    def Merge(self, firstHalf: Node, secondHalf: Node):
        if firstHalf is None:
            return secondHalf
        
        if secondHalf is None:
            return firstHalf
        
        mergedList: Node = None

        if firstHalf.value <= secondHalf.value:
            mergedList = firstHalf
            mergedList.next = self.Merge(firstHalf.next, secondHalf)
        else:
            mergedList = secondHalf
            mergedList.next = self.Merge(firstHalf, secondHalf.next)

        return mergedList


    def PrintAll(self):
        current: Node = self.head
        while current is not None:
            print(current.value)
            current = current.next


    def GetLength(self):
        return self.listLength
    

    def CountLength(self):
        count = 0
        current: Node = self.head

        while current is not None:
            count += 1
            current = current.next
    
        return count
    

    def Clear(self):
        current: Node = self.head
        
        while current is not None:
            nextNode: Node = current.next
            del current
            current = nextNode

        self.head = None
        self.tail = None
        self.listLength = 0


    def Contains(self, input_: T):
        current: Node = self.head

        while current is not None:
            if current.value == input_:
                return True
            
            current = current.next

        return False
    

    def AddAtTail(self, input: T):
        if isinstance(input, str):
            try:
                input = input.lower()
            except AttributeError:
                print("Couldn't convert to lower case")

        if self.head is None:
            self.head = Node(input)
            self.tail = self.head
        else:
            self.tail.next = Node(input)
            self.tail = self.tail.next

        self.listLength += 1


    def AddFromtextFile(self, fileLocation):
        try:
            with open(fileLocation, 'r', encoding="utf-8") as file:
                for line in file:
                    for word in line.split():
                        word = word.lower()
                        self.AddAtTail(word)
        
        except:
            print("Unable to open file. Check file path.")