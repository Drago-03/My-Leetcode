int lengthOfLongestSubstring(char* s) {
    // Array to store the last position of each character (ASCII)
    int seen[128] = {0};  // Initialize all to 0
    // Fill array with -1 to mark as unseen
    for (int i = 0; i < 128; i++) {
        seen[i] = -1;
    }
    
    int start = 0;
    int maxLength = 0;
    
    // Iterate through string
    for (int end = 0; s[end] != '\0'; end++) {
        if (seen[s[end]] >= start) {
            start = seen[s[end]] + 1;
        } else {
            int currentLength = end - start + 1;
            maxLength = (currentLength > maxLength) ? currentLength : maxLength;
        }
        seen[s[end]] = end;
    }
    
    return maxLength;
}