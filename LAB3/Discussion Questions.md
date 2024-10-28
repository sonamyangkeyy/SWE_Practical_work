## Discussion Questions
1. What are the advantages and disadvantages of the recursive approach compared to the iterative approach?
ans: 
Recursive Approach
Advantages:
          Intuitive: Aligns closely with mathematical definitions or problems that are naturally recursive.
          Cleaner Code: Often results in shorter, more readable code, focusing on the problem structure.
- Disadvantages:
          Slow: Can have poor performance (especially with overlapping subproblems) due to repeated calculations.
          Memory Intensive: Uses more stack space, which can lead to stack overflow in deep recursions.

Iterative Approach
- Advantages:
             Faster: Generally more efficient in terms of time and space, especially for simple tasks like Fibonacci.
             Stable: Does not risk stack overflow, as it uses a single function call and manages state with loops.
- Disadvantages:
             Complex: Can become complicated and harder to read for problems that are inherently recursive.
             More Code: Often requires additional variables and control structures, making it bulkier.

2. How does memoization improve the performance of the recursive function? Are there any drawbacks?
ans:
 Memoization improve the performance of the recursive function by;
     Reduces Duplicate Work:
     By storing results of previous computations, memoization prevents the same calculations from being performed multiple times.
     Enhances Speed:
     Converts functions with exponential time complexity into linear time complexity, leading to much faster execution for many recursive problems.
     Efficiency:
     Saves time by quickly retrieving previously computed results instead of recalculating them.
Drawbacks of Memoization;
     Higher Memory Consumption:
     Requires additional memory to store cached results, which can become substantial for large input sizes.
     Slight Overhead:
     The process of checking and updating the cache can introduce some performance overhead, particularly for smaller inputs where the function is fast.
     Complexity in Code:
     Implementing memoization adds complexity to the code, especially if the function deals with complex data types or has many variables.
     Memoization significantly boosts the performance of recursive functions by avoiding redundant calculations but may increase memory usage and complicate implementation.

3. In what scenarios might you prefer to use a generator function over other implementations?    
ans:
    Scenarios for Using Generators are;
    Generators are particularly useful for memory efficiency, lazy evaluation, infinite iterations, and creating clear, modular code structures.
     Efficient Memory Use:
      Ideal for large data streams where loading everything into memory is impractical; generators yield items one at a time.
     Lazy Loading:
      Generates values only when requested, making it suitable for scenarios where not all results are needed immediately.
     Handling Infinite Sequences:
      Perfect for creating infinite series (like factorials or Fibonacci) without consuming memory for all potential values.
     Performance Benefits:
      Reduces overhead by avoiding the creation of large data structures, especially when iterating over data multiple times.
     Cleaner Code Structure:
      Simplifies logic by removing the need for manual state management in iterative processes, enhancing code clarity.

4. How does the space complexity differ between these implementations?
ans:
    The space complexity differ between these implementation as generators are the most efficient in terms of space (O(1)) and iterative functions vary between O(1) and O(n) depending on data storage and Recursive functions typically use more memory (O(n)) due to stack depth.