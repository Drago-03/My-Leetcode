# 3. Longest Substring Without Repeating Characters

"""Given a string s, find the length of the longest
substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces."""
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = max_length = 0
        for end, char in enumerate(s):
            if char in seen and seen[char] >= start:
                start = seen[char] + 1
            else:
                max_length = max(max_length, end - start + 1)
            seen[char] = end
        return max_length