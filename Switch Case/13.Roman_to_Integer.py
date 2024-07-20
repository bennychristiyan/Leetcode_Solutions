#Problem
"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is 
written as XXVII, which is XX + V + II. Roman numerals are usually written largest to smallest from left to right. However, the numeral for four 
is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies 
to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4."""

# 1.Using switch case to calculate the value of the given Roman numeral to integer

# Time complexity = O(n). Runtime = 35ms (Beats 96.64%)
class Solution:
    def romanToInt(self, s: str) -> int:

        res = 0
        prev = 0

        for i in s:
            match i:
                case "I":
                    x = 1
                case "V":
                    x = 5
                case "X":
                    x = 10
                case "L":
                    x = 50
                case "C":
                    x = 100
                case "D":
                    x = 500
                case "M":
                    x = 1000
            
            # If the previous symbol has value less than the current symbol, subtract that value from the current symbol's value (x) and from the 
            # result
            if prev < x:
                x -= prev
                res -= prev

            # Add the current x to the result and also update the previous symbol value
            res += x
            prev = x

        return res 
            
# 2.Using Dictionary to calculate the value of the given Roman numeral to integer

# Time complexity = O(n). Runtime = 36ms (Beats 95.28%)
class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = 0

        for i in range(len(s)):
            # If the current symbol's value is less than it's next symbol's value, subtract the current symbol's value from the result and also
            # the next symbol's index shouldn't go above length of the given string
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            # else, add the current symbol's value to the result
            else:
                res += roman[s[i]]
        return res 

            