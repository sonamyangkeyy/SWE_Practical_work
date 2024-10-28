#Step 1
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Test the function
for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")

#Step 2
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test the function
for i in range(10):
    print(f"F({i}) = {fibonacci_iterative(i)}")

#Step 3
import time

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

# Test both functions and compare their execution times
n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n}) = {iterative_result}, Time: {iterative_time:.6f} seconds")

#Step 4
def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# Test the generator
for i, fib in enumerate(fibonacci_generator(10)):
    print(f"F({i}) = {fib}")

#Step 5
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

# Test the memoized function
for i in range(10):
    print(f"F({i}) = {fibonacci_memoized(i)}")

# Compare performance with the original recursive function
n = 30
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")


#Exercises
def fibonacci_up_to(n):
    fib_numbers = []
    a, b = 0, 1
    while a <= n:
        fib_numbers.append(a)
        a, b = b, a + b
    return fib_numbers

def index_of_first_fib_exceeding(value):
    a, b = 0, 1 
    index = 0
    while a <= value:
        a, b = b, a + b
        index += 1
    return index

def is_fibonacci_number(x):
    if x < 0:
        return False
    a, b = 0, 1
    while a < x:
        a, b = b, a + b
    return a == x

def fibonacci_ratios(n):
    ratios = []
    a, b = 0, 1
    for _ in range(n):
        if b != 0:
            ratios.append(b / a if a != 0 else float('inf'))
        a, b = b, a + b
    return ratios

n = 20 
print(f"Fibonacci numbers up to {n}: {fibonacci_up_to(n)}")
value = 15
print(f"Index of the first Fibonacci number exceeding {value}: {index_of_first_fib_exceeding(value)}")
number_to_check = 10
print(f"Is {number_to_check} a Fibonacci number? {is_fibonacci_number(number_to_check)}")
num_ratios = 11  
ratios = fibonacci_ratios(num_ratios)
print(f"Ratios of consecutive Fibonacci numbers (up to {num_ratios}): {ratios}")