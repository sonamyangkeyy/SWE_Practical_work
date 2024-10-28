#Step 1: Implement Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1 

test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search(test_list, 6)
print(f"Linear Search: Index of 6 is {result}")

#Step 2: Implement Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1 

test_list_sorted = sorted(test_list)
result = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 in sorted list is {result}")

#Step 3: Compare Performance
import time

def compare_search_algorithms(arr, target):
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time
    
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time
    
    print(f"Linear Search: Found at index {linear_result}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Time: {binary_time:.6f} seconds")

large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)

#Step 4: Implement Recursive Binary Search
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

result = binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result}")

#Step 5: Create a Main Function
def main():
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]
    
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    
    target = random.choice(test_list) 
    print(f"\nSearching for: {target}")
    
    result = linear_search(test_list, target)
    print(f"Linear Search: Found at index {result}")
    
    sorted_list = sorted(test_list)
    result = binary_search(sorted_list, target)
    print(f"Binary Search (iterative): Found at index {result}")
    
    result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (recursive): Found at index {result}")
    
    print("\nPerformance Comparison:")
    compare_search_algorithms(list(range(100000)), 99999)

if __name__ == "__main__":
    main()

##Exercises
def linear_search_all_indices(arr, target):
    indices = [] 
    for i in range(len(arr)):  
        if arr[i] == target: 
            indices.append(i)  
    return indices  
arr = [1, 4, 5, 9, 2, 2]
target = 2
result = linear_search_all_indices(arr, target)
print(f"Target {target} found at indices: {result}")


def binary_search_insertion_point(arr, target):
    left = 0 
    right = len(arr)  
    
    while left < right:  
        mid = (left + right) // 2 
        if arr[mid] < target:  
            left = mid + 1  
        else:
            right = mid 

    return left  
sorted_list = [2, 5, 6, 1, 4]
target = 4
insertion_point = binary_search_insertion_point(sorted_list, target)
print(f"The target {target} should be inserted at index: {insertion_point}")


def linear_search_count(arr, target):
    comparison_count = 0  
    for value in arr:  
        comparison_count += 1 
        if value == target:  
            return comparison_count 
    return comparison_count 

def binary_search_count(arr, target):
    left = 0 
    right = len(arr) - 1  
    comparison_count = 0 

    while left <= right:  
        mid = (left + right) // 2  
        comparison_count += 1  
        if arr[mid] < target:  
            left = mid + 1 
        elif arr[mid] > target:  
            right = mid - 1  
        else:
            return comparison_count  
            
    return comparison_count  
sorted_arr = [2, 1, 4, 8, 9]
target = 4
linear_comparisons = linear_search_count(arr, target)
print(f"Linear search comparisons: {linear_comparisons}")
binary_comparisons = binary_search_count(sorted_arr, target)
print(f"Binary search comparisons: {binary_comparisons}")



import math
import time

def jump_search(arr, target):
    n = len(arr)
    jump = int(math.sqrt(n))  
    prev = 0

    while arr[min(jump, n) - 1] < target:
        prev = jump
        jump += int(math.sqrt(n))
        if prev >= n:
            return -1  

    for i in range(prev, min(jump, n)):
        if arr[i] == target:
            return i  
    return -1  

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1

def compare_search_algorithms(arr, target):
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time

    start_time = time.time()
    binary_result = binary_search(arr, target)
    binary_time = time.time() - start_time

    start_time = time.time()
    jump_result = jump_search(arr, target)
    jump_time = time.time() - start_time

    print(f"Linear Search: Index = {linear_result}, Time = {linear_time:.6f} seconds")
    print(f"Binary Search: Index = {binary_result}, Time = {binary_time:.6f} seconds")
    print(f"Jump Search: Index = {jump_result}, Time = {jump_time:.6f} seconds")


sorted_arr = [2, 6, 7, 9, 10, 12, 13, 16, 18, 19, 22, 24, 26, 27, 29]
target = 16
compare_search_algorithms(sorted_arr, target)

