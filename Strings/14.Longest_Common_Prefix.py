#Problem
"""Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings."""

# 1.Using string and string slicing to find the longest common prefix by comparing the 1st word with the other words

# Time complexity = O(n). Runtime = 30ms
class Solution:
    def longestCommonPrefix(self, strs):
        s = ""
        # If the given list is empty, it returns ""
        if not strs:
            return s
        # Add the characters of 1st word in the list to a string 's' and compare that character with all the other words in the list, one by one
        for j in range(len(strs[0])):
            s += strs[0][j]
            for i in range(1,len(strs)):
                # If either the words in the list is smaller than the 1st word or the characters don't match, return the characters in 1st word
                # upto the matching characters
                if  j >= len(strs[i]) or strs[i][j] != s[j]:
                    return strs[0][:j]
        # If the loop ends without returning anything, return the 1st word in the list as it means every word in the list has same prefix as the
        # 1st word
        return strs[0]



# 2.Using string and list indexing to find the longest common prefix by comparing the 1st word with the other words

# Time complexity = O(n). Runtime = 41ms
class Solution:
    def longestCommonPrefix(self, strs):
        res = ""
        
        # Compare the characters of 1st word in the list with all the other words in the list, one by one
        for i in range(len(strs[0])):
            for s in strs:
                # If either the index 'i' is equal to the length of the word or the characters of 1st word does'nt match with the characters of
                # the current word, return the string 'res' (which contains the common prefix characters from previous iterations)
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            # After every iteration, add the characters of 1st word in the list to a string 'res'
            res += strs[0][i]

        return res


        

        