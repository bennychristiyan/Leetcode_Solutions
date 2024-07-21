#Problem
"""Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3."""

# 1.Using Hashmap(Dictionary) and walrus operator(:=) to find the duplicate character of the current character.

# Time complexity = O(n). Runtime = 24ms (Beats 100.00%)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        # If the length of the string s is 0, it means the string is empty, so the method returns 0 immediately as there can't be any substrings.
        if n == 0:
            return 0
        # Initialize a dictionary idx with the first character of the string s as the key and its index 0 as the value. This dictionary will 
        # keep track of the last seen index of each character in the string.
        idx = {s[0]: 0}
        # ret will store the length of the longest substring without repeating characters found so far. Since the string has at least one 
        # character (checked in the previous step), the initial longest substring has a length of 1.
        ret = 1
        curr_start = 0
        curr_len = 1
        for i in range(1, n):
            """The walrus operator :=, introduced in Python 3.8, is an assignment expression that allows you to assign a value to a variable as 
            part of an expression. This operator is useful in situations where you want to both assign and use a value in a single line of code, 
            making your code more concise and sometimes more readable.
            
            Example:
            # Traditional assignment and condition check
            n = len(data)
            if n > 10:
                print(f"Data is too long ({n} elements).")

            # Using the walrus operator
            if (n := len(data)) > 10:
                print(f"Data is too long ({n} elements).")"""
            # This line uses the walrus operator (:=) to both assign and compare j in a single step.
            # idx.get(s[i], -1) tries to get the index of the character s[i] from the idx dictionary. If the character is not found, it returns -1.
            # The condition checks if j (the last seen index of s[i]) is greater than or equal to curr_start. If it is, it means the character s[i] 
            # has been seen before within the current substring starting from curr_start.
            if (j := idx.get(s[i], -1)) >= curr_start:
                # Updates ret to be the maximum of its current value and curr_len. This is because the current substring length curr_len is a 
                # candidate for the longest substring without repeating characters found so far.
                ret = max(ret, curr_len)
                # curr_start = j + 1 updates the start of the current substring to the index right after the last occurrence of s[i]. This ensures
                # the new substring does not have repeating characters.
                curr_start = j + 1
                # curr_len = i - j updates the length of the current substring to the distance between the current index i and the last occurrence 
                # j of s[i].
                curr_len = i - j
            # If the character s[i] has not been seen within the current substring, increment the current substring length curr_len by 1.
            else:
                curr_len += 1
            # Update the idx dictionary to set the index of the current character s[i] to i. This records the latest occurrence of s[i].
            idx[s[i]] = i
        # After the loop ends, update ret one last time to ensure it holds the maximum length of the longest substring without repeating characters.
        # This is necessary in case the longest substring ends at the last character of the string s.
        ret = max(ret, curr_len)
        return ret


# 2.Using Hashmap(Dictionary) to find the duplicate character of the current character.

# Time complexity = O(n). Runtime = 41ms (Beats 98.02%)
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
    
    
# 3.Using set (or list) to remove the sequence before and the duplicate character.

# Time complexity = O(n). Runtime = 44ms (Beats 94.99%)
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
            