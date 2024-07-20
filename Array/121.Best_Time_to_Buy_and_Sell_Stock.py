#Problem
"""You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a 
single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this 
transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell."""

# 1.Using variables initiating with +ve and -ve infinity and "script execution with file I/O and standard input processing" to find the maximum 
# profit

# Time complexity = O(m * n), where m is the number of lines (Test cases) in the input and n is the average length of each list in prices
# Runtime = 83ms (Beats 99.98%)
class Solution:
    def maxProfit(prices):
        # Stores the lowest price encountered so far. Initialized to positive infinity 
        curr_buy = float("inf")
        # Stores the highest selling price after buying at curr_buy. Initialized to negative infinity 
        curr_sell = -float("inf")
        # Stores the maximum profit found so far. Initialized to negative infinity
        diff = -float("inf")

        for price in prices:
            # If the current price is lower than curr_buy, update curr_buy to this price. Reset curr_sell to negative infinity since any previous 
            # sell price is invalidated by this new lower buy price.
            if curr_buy > price:
                curr_buy = price
                curr_sell = -float("inf")
            else:
                # If the current price is higher than curr_sell, update curr_sell to this price.
                if curr_sell < price:
                    curr_sell = price
                    # Calculate the potential profit (curr_sell - curr_buy). If this profit is greater than the current diff, update diff.
                    if diff < curr_sell - curr_buy:
                        diff = curr_sell - curr_buy
        # If diff is negative (meaning no profitable transactions were found), return 0.
        if diff < 0:
            return 0
        else:
            return diff
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
        # Each parsed input is assigned to the variable 'case'
        for case in map(loads, stdin):
            # For each 'case', the 'maxProfit' function is called to compute the maximum profit.
            # The result is then written to the file 'user.out', followed by a newline character ('\n').
            f.write(f"{maxProfit(case)}\n")
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

# 2.Using variables initiating with 0 and "script execution with file I/O and standard input processing" to find the maximum profit

# Time complexity = O(m * n), where m is the number of lines (Test cases) in the input and n is the average length of each list in prices
# Runtime = 152ms (Beats 99.81%)
class Solution:
    def maxProfit(prices):
        profit = 0
        i = 0
        for j in range(i+1, len(prices)):
            # If the ith day price is greater than jth day price, update i equal to j. This means that the stock should be bought on day j because 
            # it has a lower price than the previous buying day. 
            if prices[i] > prices[j]:
                i = j
            # Updates the profit to be the maximum of the current profit and the difference between the selling price on day j and the buying 
            # price on day i.
            profit = max(profit, prices[j]-prices[i])
        return profit
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
        # Each parsed input is assigned to the variable 'case'
        for case in map(loads, stdin):
            # For each 'case', the 'maxProfit' function is called to compute the maximum profit.
            # The result is then written to the file 'user.out', followed by a newline character ('\n').
            f.write(f"{maxProfit(case)}\n")
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