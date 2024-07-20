#Problem
"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false"""

# 1.Using Hashmap(dictionary) and "script execution with file I/O and standard input processing" to find if the list of integers contain a 
# duplicate

# Time complexity = O(m * n), where m is the number of lines (Test cases) in the input and n is the average length of each list in nums
# Runtime = 50ms (Beats 99.87%)
def containsDuplicate(nums):
    dic = {}
    for i, num in enumerate(nums):
        # If the current element num is already in dic, it means that the element is a duplicate. Therefore, it returns True.
        if num in dic:
            return True
        # else, it adds num to dic with the current index i as its value.
        dic[num] = i
    # If the loop ends without returning anything, it means that there is no duplicate. Therefore, it returns False.
    return False 
"""In Python, __name__ is a special built-in variable. When a Python file is run directly, the interpreter sets __name__ to '__main__'. However, 
when a Python file is imported as a module in another script, __name__ is set to the name of the module (i.e., the filename without the .py 
extension).

Script: A Python file that is intended to be executed directly. It usually contains a main block or other code to be run when the script is 
executed. The main purpose of a script is to perform a specific task or set of tasks.

Module: A Python file intended to be imported into other Python code. It contains definitions of functions, classes, or variables that can be 
used by other scripts or modules. Modules are reusable components. When you import a module, you typically use the functions, classes, or 
variables defined in it."""
# Checks if the script is being run as the main program. If this script is imported as a module in another script, the code block under this 
# condition will not be executed. This is useful for code that should only run when the script is executed directly.
if __name__ == '__main__':
    import json, sys
    # Opens a file named 'user.out' as f in write mode ('w'). The 'with' statement ensures that the file is properly closed after the block of 
    # code is executed.
    with open('user.out', 'w') as f:
        # Iterates over each line of standard input ('sys.stdin'). 
        # map(json.loads, sys.stdin) applies the 'loads' function to each line of input. json.loads() parses a JSON string and converts it into a 
        # Python object.
        # Each parsed input is assigned to the variable 'nums'
        for nums in map(json.loads, sys.stdin):
            # Calls the containsDuplicate function with the current nums list and stores the result (True or False) in the result variable.
            result = containsDuplicate(nums)
            # Converts the result to a lowercase string ('true' or 'false'), then writes it to the file user.out.
            print(str(result).lower(), file=f)
    # Exits the script with a status code of 0, indicating successful execution.
    sys.exit()

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

# 2.Using set function and "script execution with file I/O and standard input processing" to find if the list of integers contain a 
# duplicate

# Time complexity = O(m * n), where m is the number of lines (Test cases) in the input and n is the average length of each list in nums. 
# Runtime = 63ms (Beats 99.87%)
def containsDuplicate(nums):
    return len(nums) != len(set(nums))
"""In Python, __name__ is a special built-in variable. When a Python file is run directly, the interpreter sets __name__ to '__main__'. However, 
when a Python file is imported as a module in another script, __name__ is set to the name of the module (i.e., the filename without the .py 
extension).

Script: A Python file that is intended to be executed directly. It usually contains a main block or other code to be run when the script is 
executed. The main purpose of a script is to perform a specific task or set of tasks.

Module: A Python file intended to be imported into other Python code. It contains definitions of functions, classes, or variables that can be 
used by other scripts or modules. Modules are reusable components. When you import a module, you typically use the functions, classes, or 
variables defined in it."""
# Checks if the script is being run as the main program. If this script is imported as a module in another script, the code block under this 
# condition will not be executed. This is useful for code that should only run when the script is executed directly.
if __name__ == '__main__':
    import json, sys
    # Opens a file named 'user.out' as f in write mode ('w'). The 'with' statement ensures that the file is properly closed after the block of 
    # code is executed.
    with open('user.out', 'w') as f:
        # Iterates over each line of standard input ('sys.stdin'). 
        # map(json.loads, sys.stdin) applies the 'loads' function to each line of input. json.loads() parses a JSON string and converts it into a 
        # Python object.
        # Each parsed input is assigned to the variable 'nums'
        for nums in map(json.loads, sys.stdin):
            # Calls the containsDuplicate function with the current nums list and stores the result (True or False) in the result variable.
            result = containsDuplicate(nums)
            # Converts the result to a lowercase string ('true' or 'false'), then writes it to the file user.out.
            print(str(result).lower(), file=f)
    # Exits the script with a status code of 0, indicating successful execution.
    sys.exit()

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




        




        