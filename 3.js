/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const seen = {};
    let start = 0;
    let maxLength = 0;
    
    [...s].forEach((char, end) => {
        if (char in seen && seen[char] >= start) {
            start = seen[char] + 1;
        } else {
            maxLength = Math.max(maxLength, end - start + 1);
        }
        seen[char] = end;
    });
    
    return maxLength;
};

// Create instance and call method
const param_1 = "abcabcbb"; // example input
const ret = lengthOfLongestSubstring(param_1);

module.exports = lengthOfLongestSubstring;