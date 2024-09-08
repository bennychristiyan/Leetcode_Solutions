"""Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1."""

# 1.Using curSum & maxSum concept and "script execution with file I/O and standard input processing" to find the maximum sum of subArray of the
# list

# Time complexity = O(n), where n is the length of the list nums
# Runtime = 73ms (Beats 99.99%)

from sys import stdin
from json import loads
def solve():
    # This opens a file called 'user.out' in write mode ('w'). If the file already exists, it will be overwritten. All the results (max subarray 
    # sums) will be written to this file.
    f = open('user.out', 'w')
    # Iterates over each line of standard input ('stdin'). 
    # map(loads, stdin) applies the 'loads' function to each line of input. loads() parses a JSON string and converts it into a Python object.
    # Each parsed input is assigned to the variable 'nums'
    for nums in map(loads, stdin):
        # Initialize two variables: maxSum and curSum, both set to the first element of the array nums.
        # maxSum keeps track of the largest sum of any subarray encountered so far.
        # curSum is the sum of the current subarray being evaluated.
        maxSum, curSum = nums[0], nums[0]
        # This loop iterates through the rest of the array nums starting from the second element (since nums[1:] skips the first element).
        for num in nums[1:]:
            # If curSum is negative, we reset it to the current number num, effectively starting a new subarray from this point.
            if curSum < 0:
                curSum = num
            # If curSum is not negative, we continue with the current subarray by adding the current number (num) to curSum.
            else:
                curSum += num
            # If the updated curSum is greater than the current maxSum, then set maxSum to the new, larger curSum..
            if curSum > maxSum:
                maxSum = curSum
        # Write the maximum subarray sum (maxSum) for this input to the output file 'user.out'.
        print(maxSum, file=f)
# This calls the solve function, which runs the logic described above.
solve()
# This exits the program after the function has completed, ensuring no further code is executed.
exit()

"""1.Efficient Input Handling:
Using 'map(loads, stdin)' allows for efficient parsing of input data. Each line of input is processed as soon as it's read, which can be more 
memory-efficient than reading all input at once, especially for large inputs.

2.Efficient Output Handling:
Writing results to a file within the loop ensures that results are written incrementally, rather than storing them all in memory and writing them 
at the end. This can be more efficient in terms of memory usage.
    
Including additional code to handle input and output, which wraps the maxProfit function means it can process multiple test cases from a standard 
input and write results to a file."""

"""JSON, which stands for JavaScript Object Notation, is a lightweight data-interchange format that's easy for humans to read and write, and easy 
for machines to parse and generate. It is often used to transmit data between a server and a web application or between different systems.

JSON format consists of two main structures:

1.Objects: A collection of key-value pairs enclosed in curly braces {}. Each key is a string, and the value can be a string, number, object, array,
true, false, or null. Key-value pairs are separated by commas.

Example:
{
  "name": "John",
  "age": 30,
  "city": "New York"
}

2.Arrays: An ordered list of values enclosed in square brackets []. Values can be strings, numbers, objects, arrays, true, false, or null, and are
separated by commas.

Example:
["apple", "banana", "cherry"]"""

# 2.Using curSum & maxSub concept and "script execution with file I/O and standard input processing" to find the maximum sum of subArray of the
# list

# Time complexity = O(n), where n is the length of the list nums
# Runtime = 104ms (Beats 99.91%)

def maxSubArray(nums):
    # This initializes maxSub with the first element of the array nums. maxSub will store the maximum sum encountered during each iteration.
    maxSub = nums[0]
    # This initializes curSum to 0. curSum will track the sum of the current subarray being considered.
    curSum = 0
    for i in nums:
        # If the current subarray sum (curSum) is negative, it is better to start fresh, as continuing with a negative sum will reduce the total 
        # sum of any subarray. Hence, reset curSum to 0, indicating that a new subarray will start from the current element i.
        if curSum < 0:
            curSum = 0
        # Add the current element i to curSum. This extends the current subarray by including i.
        curSum += i
        # Update maxSub with the larger of the current maxSub or curSum. This ensures that maxSub always holds the maximum sum encountered during 
        # each iteration.
        maxSub = max(maxSub, curSum)
    return maxSub
"""In Python, __name__ is a special built-in variable. When a Python file is run directly, the interpreter sets __name__ to '__main__'. 
However, when a Python file is imported as a module in another script, __name__ is set to the name of the module (i.e., the filename without 
the .py extension).
    
Script: A Python file that is intended to be executed directly. It usually contains a main block or other code to be run when the script is 
executed. The main purpose of a script is to perform a specific task or set of tasks.

Module: A Python file intended to be imported into other Python code. It contains definitions of functions, classes, or variables that can be 
used by other scripts or modules. Modules are reusable components. When you import a module, you typically use the functions, classes, or 
variables defined in it."""
# Checks if the script is being run as the main program. If this script is imported as a module in another script, the code block under this 
# condition will not be executed. This is useful for code that should only run when the script is executed directly.
if __name__ == "__main__":
    from sys import stdin
    from json import loads
    # Opens a file named 'user.out' as f in write mode ('w'). The 'with' statement ensures that the file is properly closed after the block of 
    # code is executed.
    with open('user.out', 'w') as f:
        # Iterates over each line of standard input ('stdin'). 
        # map(loads, stdin) applies the 'loads' function to each line of input. loads() parses a JSON string and converts it into a Python object.
        # Each parsed input is assigned to the variable 'nums'
        for nums in map(loads, stdin):
            # For each 'nums', the 'maxSubArray' function is called to compute the maximum sum of the sub array of the array.
            # The result is then written to the file 'user.out', followed by a newline character ('\n').
            # replace(" ","") method replaces all spaces (" ") in the string with nothing ("").
            f.write(f"{maxSubArray(nums)}\n".replace(" ",""))
    # Terminates the program with an exit status of `0`, indicating successful execution.
    exit(0) 


"""1.Efficient Input Handling:
Using 'map(loads, stdin)' allows for efficient parsing of input data. Each line of input is processed as soon as it's read, which can be more 
memory-efficient than reading all input at once, especially for large inputs.

2.Efficient Output Handling:
Writing results to a file within the loop ensures that results are written incrementally, rather than storing them all in memory and writing them 
at the end. This can be more efficient in terms of memory usage.
    
Including additional code to handle input and output, which wraps the maxProfit function means it can process multiple test cases from a standard 
input and write results to a file."""

"""JSON, which stands for JavaScript Object Notation, is a lightweight data-interchange format that's easy for humans to read and write, and easy 
for machines to parse and generate. It is often used to transmit data between a server and a web application or between different systems.

JSON format consists of two main structures:

1.Objects: A collection of key-value pairs enclosed in curly braces {}. Each key is a string, and the value can be a string, number, object, array,
true, false, or null. Key-value pairs are separated by commas.

Example:
{
  "name": "John",
  "age": 30,
  "city": "New York"
}

2.Arrays: An ordered list of values enclosed in square brackets []. Values can be strings, numbers, objects, arrays, true, false, or null, and are
separated by commas.

Example:
["apple", "banana", "cherry"]"""
        