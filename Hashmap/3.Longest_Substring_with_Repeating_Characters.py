#Problem
"""Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3."""

# 1.Using Hashmap(Dictionary) to find the duplicate character of the current character. If the current character is not present in the dictionary
# or the index value of the duplicate character is less than start, that character is stored as key and it's index(end) is stored as value; else
# update start by adding 1 to the index of the duplicate character (as to start from the next character to the duplicate character) and it's
# character is stored as key and it's index(end) is stored as value. The max length is also calculated during each iteration and is returned after
# the loop ends

# Time complexity = O(n). Runtime = 49ms
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dic = {}
        max_length = 0
        start = 0

        for end, char in enumerate(s):
            if char in my_dic and my_dic[char] >= start:
                # Move the start to the right of the last occurrence of the duplicate character
                start = my_dic[char] + 1
            # Update the character's latest index
            my_dic[char] = end
            # Calculate the length of the current substring
            max_length = max(max_length, end - start + 1)

        return max_length
    
    
# 2.Using set (or list) to remove the sequence before and the duplicate character. If the current character is not present in the set, that
# character is added to the set (or list); else remove the characters from the left of the set (or list), until the duplicate character is present 
# in the set (or list) by updating the 'l' during each iteration and that character is added to the set (or list). The max length is also 
# calculated during each iteration and is returned after the loop ends

# Time complexity = O(n). Runtime = 58ms            
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets = set() # or []
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in sets:
                sets.remove(s[l])
                l += 1
            
            sets.add(s[r])
            res = max(res, r - l + 1)
        return res
            