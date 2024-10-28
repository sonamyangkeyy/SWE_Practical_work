# SWE_Practical_work
## LAB2
# Exercises
Lowercase Conversion: This ensures that "Word" and "word" are considered the same.
Splitting: The split() method breaks the text into words.
Set for Uniqueness: A set automatically handles duplicates.
Count: The length of the set gives the number of unique words.

-find_longest_word Function:
It splits the text into words.
It uses max() with key=len to find the longest word.
The program counts unique words and finds the longest word in the provided text.

count_word_occurrences Function:
Converts both the input text and the target word to lowercase for case-insensitive comparison.
Splits the text into words and uses the count() method to count how many times the target word appears.

calculate_average_word_length Function:
Calculates the average length of words by summing their lengths and dividing by the total number of words.
percentage_of_long_words Function:
Uses the average word length to determine which words are longer than that average.
Calculates the percentage of these long words compared to the total number of words.

## LAB3
# Exercises
- fibonacci_up_to(n):
This function generates a list of Fibonacci numbers up to a specified limit n.

- index_of_first_fib_exceeding(value):
This function returns the index of the first Fibonacci number that exceeds a given value.

- is_fibonacci_number(x):
This function checks if a given number x is a Fibonacci number by generating Fibonacci numbers until it either finds x or exceeds it.

- fibonacci_ratios(n):
This function calculates the ratios of consecutive Fibonacci numbers and returns them in a list, showing how they approach the golden ratio.

we can specify the value of n to get Fibonacci numbers.

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

