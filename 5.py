#5. Longest Palindromic Substring

"""Given a string s, return the longest
palindromic
substring
in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

 

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start = 0
        max_length = 1
        
        # Helper function to expand around center
        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        for i in range(len(s)):
            # Odd length palindrome
            len1 = expand_around_center(i, i)
            # Even length palindrome
            len2 = expand_around_center(i, i + 1)
            
            length = max(len1, len2)
            if length > max_length:
                start = i - (length - 1) // 2
                max_length = length
        
        return s[start:start + max_length]