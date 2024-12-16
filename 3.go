func lengthOfLongestSubstring(s string) int {
    seen := make(map[rune]int)
    start := 0
    maxLength := 0
    
    for end, char := range s {
        if lastSeen, ok := seen[char]; ok && lastSeen >= start {
            start = lastSeen + 1
        } else {
            if current := end - start + 1; current > maxLength {
                maxLength = current
            }
        }
        seen[char] = end
    }
    
    return maxLength
}