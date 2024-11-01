#Step 1: Define the Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Step 2: Create the LinkedList Class
class LinkedList:
    def __init__(self):
        self.head = None

#Step 3: Implement the Append Method
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()  

#Step 4: Implement the Display Method
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  

# Step 5: Implement the Insert Method
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.insert(4, 1)
ll.display()  

#Step 6: Implement the Delete Method
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.insert(4, 1)  
ll.display()      
ll.delete(2)     
ll.display()      

# Step 7: Implement the Search Method
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.insert(4, 1)  
ll.display()      
print(ll.search(4))  
print(ll.search(5))  
ll.delete(2)    
ll.display()      

#Step 8: Implement the Reverse Method
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.insert(4, 1) 
ll.display()   
print(ll.search(4))  
print(ll.search(5))  
ll.delete(2)     
ll.display()      
ll.reverse()     
ll.display()      


##Exercises 
#1
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next        
        fast = fast.next.next   
    return slow.value 
head = ListNode(3, ListNode(6, ListNode(9, ListNode(12, ListNode(15)))))
print(find_middle(head)) 

#2
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    visited = set()
    current = head   
    
    while current:  
        if current in visited:  
            return True  
        visited.add(current)  
        current = current.next  
    
    return False  

#3
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def remove_duplicates(head):
    if not head:
        return head 

    # Step 1: Convert the linked list to an array
    current = head
    values = []
    
    while current:
        values.append(current.value) 
        current = current.next

    values.sort()

    if not values:
        return None

    new_head = ListNode(values[0]) 
    new_current = new_head

    for value in values[1:]:  
        if value != new_current.value: 
            new_current.next = ListNode(value)
            new_current = new_current.next

    return new_head 

#4
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_two_sorted_lists(l1, l2):
    # Step 1: Create a dummy node
    dummy = ListNode(0)
    current = dummy  # Pointer to build the new merged list

    # Step 2: Initialize pointers for both lists
    p1, p2 = l1, l2

    # Step 3: Iterate and compare nodes from both lists
    while p1 and p2:
        if p1.value < p2.value:
            current.next = p1  
            p1 = p1.next  
        else:
            current.next = p2  
            p2 = p2.next  
        current = current.next  

    # Step 4: Handle remaining elements
    if p1:  
        current.next = p1
    elif p2: 
        current.next = p2

    return dummy.next
