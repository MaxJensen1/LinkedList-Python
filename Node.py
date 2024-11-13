from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Node(Generic[T]):
    # Construtor. This apparently creates a value of type T that is public by default
    def __init__(self, value: T, next: Optional['Node[T]'] = None): # Sets value to T input, and next to null
        self.value: T = value  # The value of the node
        self.next: Optional[Node[T]] = next