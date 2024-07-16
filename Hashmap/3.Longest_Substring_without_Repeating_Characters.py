#Problem
"""Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3."""

# 1.Using Hashmap(Dictionary) to find the duplicate character of the current character.

# Time complexity = O(n). Runtime = 49ms
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dic = {} #character(key) : index(value)
        max_length = 0
        start = 0

        for end, char in enumerate(s):
            # If the current character is present in the dictionary and the index value of the duplicate character is equal to or greater than 
            # start, update start by adding 1 to the index of the duplicate character (as to start from the next character to the duplicate 
            # character)
            if char in my_dic and my_dic[char] >= start:
                start = my_dic[char] + 1
            # The current character is stored as key and it's index(end) is stored as value
            my_dic[char] = end
            # Calculate the length of the current substring
            max_length = max(max_length, end - start + 1)
        return max_length
    
    
# 2.Using set (or list) to remove the sequence before and the duplicate character.

# Time complexity = O(n). Runtime = 58ms            
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets = set() # or []
        l = 0
        res = 0

        for r in range(len(s)):
            # If the current character is present in the set, remove the characters from the left of the set (or list), until the duplicate 
            # character is present in the set (or list) by updating the 'l' during each iteration
            while s[r] in sets:
                sets.remove(s[l])
                l += 1
            # else, that character is added to the set (or list)
            sets.add(s[r])
            # Calculate the length of the current substring
            res = max(res, r - l + 1)
        return res
            