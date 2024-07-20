#Problem
"""Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left."""

# 1.Using 'i', 'j' pointers to check if the mirror character of each character is same.

# Time complexity = O(n). Runtime = 40ms (Beats 96.31%)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 'i' starts from left and 'j' starts from right
        i = 0
        j = len(s) - 1
        # x is converted into a string
        s = str(x)

        while i <= j:
            # If 'i' and 'j' point to same character, update 'i' by adding 1 and 'j' by subtracting 1 until 'i' becomes greater than 'j'
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

# 2.Using string slicing, compare the original string with the inversed string.  

# Time complexity = O(n). Runtime = 42ms (Beats 94.15%)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x is converted into a string
        s = str(x)
        return s == s[::-1]

# 3.Using left, right pointers to check if MSB and LSB are same. 

# Time complexity = O(n). Runtime = 58ms (Beats 39.42%)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Returns False, if negative
        if x < 0: return False

        # Identifies the MSB place of x
        div = 1
        while x >= 10 * div:
            div *= 10

        while x:
            # Returns the LSB
            right = x % 10
            # Returns the MSB
            left = x // div

            if left != right: return False

            # x % div --> removes MSB and // 10 --> removes LSB
            x = (x % div) // 10
            # Since, 2 digits are removed, the div is divided by 100
            div /= 100
        
        return True

        