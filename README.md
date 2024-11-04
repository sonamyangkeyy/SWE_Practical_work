# SWE_Practical_work
## LAB2
# Exercises
Lower casing : Make "Word" and "word" treated as one.
Splitting — The split() method divides the given text into words.
Create a set for uniqueness: There is no special set() like function in other languages; a Python set will just discard duplicates.
Count: Total number of unique words by finding the length of the set.

-find_longest_word Function:
The text : Tokenization. This means it divides the text into words.
It uses max() with key=len to get the longest word.
This program counts the number of unique words and also finds the longest word from the given text.
You have until October 2023 available data, You will assets problems related to this, count_word_occurrences Function.
Changes the input string as well as the word to be searched into lower case.
It splits the text into words and counts how many times the target word appears using count() method.
Let's break down the code snippet above, 'calculate_average_word_length' Function:-
Average word length

## LAB3
# Exercises
fibonacci_up_to(n):
This function makes lists of Fibonacci numbers less than or equal to the input number n.’’
index_of_first_fib_exceeding(value):
This function finds the sequential Fibonacci number that is the first to exceed the input number value.
is_fibonacci_number(x):
The function checks whether “x” is a Fibonacci number, by generating Fibonacci numbers until it finds x or exceeds it.
fibonacci_ratios(n):
This function finds the ratios of Fibonacci numbers and returns the computed array in a way that demonstrates its convergence to the golden ratio.
n can be treated as cutoff point for the Fibonacci numbers.



## LAB4
# Exercises
 1. Initialization: We start with an empty list called indices to store the indices of the target.
    Loop: We loop through the list arr using range(len(arr)), which gives us the index i.
    Condition Check: Inside the loop, we check if the current element arr[i] is equal to target.
    Appending Indices: If they match, we add the index i to the indices list.
    Return Result: Finally, we return the list of indices.


 2. left starts at 0 (the beginning of the list).
    right starts at the length of the list (which points just past the last element).
    The while loop runs as long as left is less than right.
    mid is calculated to find the middle index of the current range.
    If the value at the mid index is less than the target, the target must be to the right, so we adjust left to mid + 1.
    If the value at mid is greater than or equal to the target, we adjust right to mid, keeping the target in the left portion of the range.
    When the loop ends, left indicates where the target should be inserted to keep the list sorted.

 3. Linear Search:
    The function linear_search_count initializes a counter to zero.
    It loops through each element in the list, incrementing the counter for each comparison.
    If the target is found, it returns the count; if the loop completes without finding the target, it returns the count.
    Binary Search:
    The function binary_search_count uses two pointers, left and right, to define the search range.
    It calculates the middle index and increments the comparison count for each check.
    Depending on the comparison with the middle element, it adjusts the search range.
    Returns the count when the target is found or when the search concludes without finding it.

 4. Jump Search:Jumps ahead by the square root of the array size to find a block where the target might be.
    Then performs a linear search within that block.
    Linear Search:Checks each element one by one.
    Binary Search:Divides the search range in half repeatedly.
    Performance Comparison:Measures and prints the time taken and index found for each search method.

## LAB5
# Exercises

1.  Stack Usage: An empty stack is created to hold numbers.
    Token Processing:
    The expression is split into tokens (numbers and operators).
    Numbers are pushed onto the stack.
    For operators, the top two numbers are popped, and the operation is performed.
    Final Result: The last remaining number in the stack is the result of the expression.

2.  Two Stacks: Use stack1 for adding items and stack2 for removing them.
    Enqueue: Push items onto stack1.
    Dequeue: If stack2 is empty, move all items from stack1 to stack2 before popping from stack2.

3.  Queue: Uses a deque to manage tasks.
    Add Task: Adds tasks to the end of the queue.
    Run Tasks: Processes and removes tasks in FIFO order.

4.  Precedence: A dictionary to handle operator precedence.
    Stack and Output: Operators go to the stack; operands go to the output list.
    Final Processing: Remaining operators in the stack are appended to the output. 

## LAB6
# Exercises
# 1
1.ListNode Class: Represents each node in the linked list, holding a value and a reference to the next node.

2.Two Pointers:
Each time, the slow one moves one step. Two steps at a time are moved by the fast one.

3.Traversal:
By one, and two, slow and fast are moved when steps are taken and fast, and fast.next are not null. At the end when reached by fast, slow is in the middle. The value at the slow pointer which is the middle element, is returned.

Time Complication is considered.  
O(n): The list is traversed once.  
Space Complication  
O(1): Only two pointers are used, regardless of the list's size.

# 2
1.Node Definition: The ListNode class represents each node in the linked list.

2.Function Definition: The has_cycle function checks for a cycle:
We create an empty set called visited to store nodes we encounter.

3.While Loop:
The loop continues as long as current is not None.
Inside the loop:
We check if the current node is already in the visited set.
If it is, we return True because we have detected a cycle.
If not, we add the current node to the visited set and proceed to the next node.

4.End of List: If we finish traversing the list and don’t find any duplicates, we return False, indicating there’s no cycle.

# 3
1.Node Definition: The ListNode class defines each node in the linked list.

2.Function Definition: The remove_duplicates function performs the following:
Base Case: If the linked list is empty (head is None), return head.
Convert to Array: Traverse the linked list and collect all values into a list called values.

3.Sorting: Use Python’s built-in sort() method to sort the values array.

4.Rebuild the Linked List:
Start by creating a new head node with the first value in the sorted array.
Loop through the sorted values starting from the second element.
If the current value is not equal to the last added value in the new linked list, create a new node and link it.

5.Return Statement: Finally, return the new linked list starting from new_head.

# 4
1.Node Definition: The ListNode class is defined with a constructor that initializes the value and the pointer to the next node.

2.Function Definition: The merge_two_sorted_lists function is defined to merge two sorted linked lists:

Dummy Node: A dummy node is created to facilitate easy list building. The merged list will start from dummy.next.
Current Pointer: current is initialized to point to the dummy node. This pointer will help us build the merged list.

3.Pointer Initialization: p1 and p2 are initialized to point to the heads of the input lists l1 and l2.

4.While Loop:
The loop continues as long as both p1 and p2 point to valid nodes (not None).
Inside the loop, we compare the values of the nodes pointed to by p1 and p2:
If p1.value is smaller, we set current.next to p1, effectively appending p1 to the merged list, and move p1 to the next node.
If p2.value is smaller or equal, we set current.next to p2, append p2, and move p2 to the next node.
After linking a node, we move current to current.next to continue building the merged list.

5.Remaining Elements Handling: After the loop, if there are remaining nodes in either p1 or p2, we append the non-exhausted list directly to current.next.

6.Return Statement: Finally, the function returns dummy.next, which is the head of the newly merged list, skipping the dummy node.

## LAB7
# Exercises
# 1
1.TreeNode Class: This class represents a single node in the BST, which includes:
A value that holds the node's data.
Pointers to left and right children.

2. BST Class:
insert Method:
This method adds a new value to the BST.
If the tree is empty, it creates the root node.
It uses the _insert_rec method to place the new value in the correct position based on the BST properties.

3.Finding the Maximum Value:
Public Method find_max:
This method checks if the tree has a root. If not, it returns None, indicating the tree is empty.
If the root exists, it calls _find_max with the root node.
Private Method _find_max:
It initializes current to the given node (starting from the root).
A while loop traverses to the right child until there are no more right children (i.e., current.right is None).
Once the loop exits, current points to the rightmost node, which contains the maximum value.
The method then returns this maximum value.

Key Concepts
BST Structure: A BST is structured so that for any given node, all values to the left are smaller, and all values to the right are larger.
Maximum Value Location: The rightmost node will always have the maximum value in a BST due to the ordering property.

Complexity
Time Complexity: O(h), where h is the height of the tree. In the worst-case scenario (for an unbalanced tree), this could degrade to O(n) if the tree is skewed.
Space Complexity: O(1) for the iterative method, as it does not use additional data structures.

# 2
1.TreeNode Class: Each node has a value and pointers to left and right children.

2.BST Class:
insert Method: Adds values while maintaining the BST properties.
count_nodes Method: Calls a recursive helper to count nodes.

3.Counting Logic:
Recursive Helper Function:
Returns 0 if the node is None (base case).
Returns 1 for the current node plus counts from left and right children.

Complexity
Time Complexity: O(n) since it visits every node.
Space Complexity: O(h) due to recursion, where h is the height of the tree.

# 3
1.TreeNode Class: Represents each node with a value and pointers to its left and right children.

2.BST Class:
insert Method: Inserts a value into the BST, maintaining the order.
level_order_traversal Method: Executes the level-order traversal.

3.Traversal Process:
Use a queue to keep track of nodes to visit, starting with the root.
While there are nodes in the queue:
Dequeue the front node and append its value to the result list.
Enqueue its left and right children if they exist.

4.Return the Result: The method returns a list of node values in level order.

Complexity
Time Complexity: O(n) because each node is visited once.
Space Complexity: O(w), where w is the maximum width of the tree (number of nodes at the widest level).

# 4
1.TreeNode Class: Represents each node in the BST with a value, and pointers to left and right children.

2.BST Class:
insert Method: Inserts a new value while maintaining the BST properties.
height Method: Public method to calculate the height of the tree.

3.Height Calculation:
Recursive Function _height_rec:
Base Case: If the node is None, return -1. This indicates that the height of an empty tree is considered -1.
The function recursively calculates the heights of the left and right subtrees.
The height of the current node is computed as 1 + max(left_height, right_height), where 1 accounts for the current node.

Complexity
Time Complexity: O(n), where n is the number of nodes, since every node must be visited to calculate the height.
Space Complexity: O(h), where h is the height of the tree, due to the recursion stack.

# 5
1.TreeNode Class: Represents a node in the BST, containing a value and references to left and right children.

2.BST Class:
insert Method: Adds a new value to the BST, maintaining the order.
is_valid_bst Method: Public method to start the validity check.
3.Validation Logic:
Recursive Function _is_valid_bst_rec:
Base Case: If the node is None, return True because an empty subtree is valid.
Check Left Subtree: Recursively call the function for the left child before checking the current node.
Current Node Check: Compare the current node’s value with the last visited value:
If the current node's value is less than or equal to last_value, the BST property is violated, and we return False.
Update Last Visited Value: Set last_value to the current node's value.
Check Right Subtree: Recursively check the right child.

Complexity
Time Complexity: O(n), where n is the number of nodes, since each node is visited once.
Space Complexity: O(h), where h is the height of the tree, due to recursion.

## LAB8
# Exercises
# 1
In-Place: Uses the same array in order to sort it. Time complexity: Average o(nlog n), worst o(n2). Space complexity: o(log n)due to recursion.

# 2
Early Exit: Stops sorting if there are no changes made during a pass-through.
Efficiency: It is better suited for the cases where the array is nearly sorted.

# 3
Insertion Sort: Small subarrays are well handled especially when they are smaller than or equal to 10.
Merge Sort: Organizes larger arrays, thus improving the general performance.
Hybrid Approach: The flow enhanced scheme combines the algorithm of both First flow and Improved flow for the most efficiency.

# 4
Bubble Sort: Enables visualization of every swap performed in the course of sorting.
Merge Sort: Explains how merging of subarrays is done.
Animation: The sorting steps are made obvious by bar charts.


## LAB9
# Exercises
# 1
This code is a class called Graph, which creates a simple undirected graph where we can add edges, print the struct, BFS through the graph, and find the shortest path between two nodes.
Key Components
Graph Initialization:
Graph is in form of dictionary with keys that are vertices while values in the list are the neighboring vertices of the key ( self.graph).

Adding Edges:
The has_model member function returns whether or not there is a model specified; it takes no arguments and returns a boolean value, while the add_edge(u, v) method creates an undirected edge between the vertices u and v.

Printing the Graph:
Each vertex and neighbors are printed by the print_graph() method.

Breadth-First Search (BFS):
The bfs(start) method traverses the graph from the start vertex to all other vertex and prints the vertex it visits.

Finding the Shortest Path:
The required shortest_path(start, end) utilises the BFS algorithm to find and output the shortest path from the start node to the end or None otherwise.

# 2
Graph Initialization: Graph DB is in the form of an adjacency list for a set of keys.
Adding Edges: Edges are created by the add_edge method.
Cycle Detection: Thus, the has_cycle method has been designed to use the Depth First Search (DFS) to look for cycles. It simply tags vertices as visited and also makes a check if a vertex has been visited that is not the parent.
Example Usage: Finally, the method adds edges, looks for cycles and then prints the result.

# 3
Graph Representation: Specifically, the graph is needed to be stored as an adjacency list containing not only the info about the edges but also the extra weights.
Dijkstra's Algorithm: Uses a priority queue to determine the least cost path from a start node to all other nodes.
Output: Returns a dictionary of the shortest distances from the starting vertex given as an attribute.

# 4
Graph Representation:
In this representation the graph is an adjacency list, which means that keys are vertices, and values are lists of adjacent vertices.
Bipartite Check Using BFS:
The is_bipartite() method starts with color_dict to keep the tracks of the colors occurred for each vertex.
For each uncolored vertex, it starts a BFS:
Colors the starting vertex.
For each neighbor, it checks:
If it is not colored, it assigns the current color (alternate) and enQueue it.
If already colored with the same color as the current vertex, IT RETURNS False as it means that the graph is not bipartite.

