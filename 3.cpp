#include <string>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        std::unordered_map<char, int> seen;
        int start = 0;
        int maxLength = 0;
        
        for (int end = 0; end < s.length(); end++) {
            if (seen.find(s[end]) != seen.end() && seen[s[end]] >= start) {
                start = seen[s[end]] + 1;
            } else {
                maxLength = std::max(maxLength, end - start + 1);
            }
            seen[s[end]] = end;
        }
        
        return maxLength;
    }
};