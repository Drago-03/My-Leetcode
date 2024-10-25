# 22. Generate Parentheses

"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(s='', open_count=0, close_count=0):
            if len(s) == 2 * n:
                result.append(s)
                return
            if open_count < n:
                backtrack(s + '(', open_count + 1, close_count)
            if close_count < open_count:
                backtrack(s + ')', open_count, close_count + 1)
        
        backtrack()
        return result
