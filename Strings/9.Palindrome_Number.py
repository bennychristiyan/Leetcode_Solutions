"""Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left."""

# 1.Using string slicing, compare the original string with the inversed string.  

# Time complexity = O(n). Runtime = 47ms
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]


# 2.Using 'i', 'j' pointers to check if the mirror character of each character is same. The given number is converted into a string. 'i' starts 
# from left and 'j' starts from right. If 'i' and 'j' point to same character, update 'i' by adding 1 and 'j' by subtracting 1; else return False.
# After 'i' becomes greater than 'j', return True

# Time complexity = O(n). Runtime = 48ms
class Solution:
    def isPalindrome(self, x: int) -> bool:
        i = 0
        s = str(x)
        j = len(s) - 1

        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
    

        