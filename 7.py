# 7. Reverse Integer

"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

 

Constraints:

    -231 <= x <= 231 - 1

"""

class Solution:
    def reverse(self, x: int) -> int:
        # Handle the sign separately
        sign = 1 if x > 0 else -1
        x = abs(x)
        
        # Reverse the digits
        reversed_num = 0
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        # Apply the sign
        result = sign * reversed_num
        
        # Check if the result is within the 32-bit integer range
        if result > 2**31 - 1 or result < -2**31:
            return 0
        
        return result