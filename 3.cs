public class Solution {
    public int LengthOfLongestSubstring(string s) {
        Dictionary<char, int> seen = new Dictionary<char, int>();
        int start = 0;
        int maxLength = 0;
        
        for (int end = 0; end < s.Length; end++) {
            char currentChar = s[end];
            if (seen.ContainsKey(currentChar) && seen[currentChar] >= start) {
                start = seen[currentChar] + 1;
            } else {
                maxLength = Math.Max(maxLength, end - start + 1);
            }
            seen[currentChar] = end;
        }
        
        return maxLength;
    }
}