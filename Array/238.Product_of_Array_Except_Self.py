"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. 
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and 
without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]"""

# 1.Using try except blocks and "script execution with file I/O and standard input processing" to find the result of list containing either single 
# 0 or more than one 0's or without any 0's

# Time complexity = O(n), where n is the length of the list nums
# Runtime = 68ms (Beats 99.99%)

def product_of(nums):
    result = 1
    for i in nums:
        result *= i
    return result

def canCompleteCircuit(nums):
    # This block is used to attempt code that might throw an exception, specifically in cases where the number 0 might not be in the list.
    try:
        # The function tries to find the index of the first occurrence of 0 in the list nums using the index method. If no 0 is found, it will 
        # raise a ValueError, which will be caught by the except block.
        i_1 = nums.index(0)
        # This inner try block is attempting to find the second occurrence of 0.
        try:
            size = len(nums)
            tmp = [0] * size
            # This line attempts to find the index of the second occurrence of 0 in the list nums, starting the search from i_1 + 1. If no second 
            # 0 is found, a ValueError will be raised.
            i_2 = nums.index(0, i_1+1)
            # If the second 0 is found, the function simply returns the zero-filled list tmp.
            return tmp
        # This block is executed if no second 0 is found. Here, the function will perform a special calculation for the list containing only one 0.
        except:
            size = len(nums)
            tmp = [0] * size
            # The function calculates the product of all elements in nums except the 0 at index i_1. This is done by taking two slices of nums:
            # one before i_1 (nums[:i_1]) and one after i_1 (nums[i_1+1:]), and passing them to the product_of function. The result is then
            # assigned to tmp[i_1].
            tmp[i_1] = product_of(nums[:i_1]+nums[i_1+1:])
            # The modified tmp list is returned.
            return tmp
    # This except block is executed if there are no zeros in nums (i.e., the initial index(0) call failed).
    except:
        # The product_of function is called to calculate the product of all elements in nums.
        product = product_of(nums)
        # This list comprehension divides the total product by each element i in nums. This effectively gives the product of all elements except 
        # i for each i. The result is returned as a list.
        return [int(product/i) for i in nums]
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
            # For each 'nums', the 'canCompleteCircuit' function is called to compute the product of the array except itself.
            # The result is then written to the file 'user.out', followed by a newline character ('\n').
            # replace(" ","") method replaces all spaces (" ") in the string with nothing ("").
            f.write(f"{canCompleteCircuit(nums)}\n".replace(" ",""))
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

# 2.Using prefix & postfix concept and "script execution with file I/O and standard input processing" to find the result by multiplying the prefix
# and postfix of every element in the list

# Time complexity = O(n), where n is the length of the list nums
# Runtime = 79ms (Beats 99.94%)

def productExceptSelf(nums):
    # prefix and postfix are initialized to 1. These variables will store the product of numbers encountered so far when traversing nums in two 
    # directions (left-to-right and right-to-left).
    prefix, postfix = 1, 1
    answer = [1] * len(nums)
    # First for loop (Left-to-right traversal). This loop ensures that answer[i] will have the product of all elements to the left of nums[i] 
    # after it completes.
    for i in range(len(nums)):
        # The current value of prefix (product of all elements before nums[i]) is multiplied with answer[i] and stored back into answer[i].
        answer[i] *= prefix
        # prefix is then updated by multiplying it with nums[i]. This prepares prefix to store the product of elements up to the next index.
        prefix *= nums[i]
    # Second for loop (Right-to-left traversal (len(nums) - 2 to 0)). After this loop finishes, answer[j] will hold the product of all elements both to the left and 
    # right of nums[j], which is the desired result.
    for j in range(len(nums)-2, -1, -1):
        # postfix is updated by multiplying it with nums[j+1] (i.e., the element to the right of nums[j]).
        postfix *= nums[j+1]
        # The current value of postfix (product of all elements after nums[j]) is multiplied with answer[j] and stored back into answer[j].
        answer[j] *= postfix
    return answer
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
            # For each 'nums', the 'canCompleteCircuit' function is called to compute the product of the array except itself.
            # The result is then written to the file 'user.out', followed by a newline character ('\n').
            # replace(" ","") method replaces all spaces (" ") in the string with nothing ("").
            f.write(f"{productExceptSelf(nums)}\n".replace(" ",""))
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

