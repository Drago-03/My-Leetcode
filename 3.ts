function lengthOfLongestSubstring(s: string): number {
    const seen: { [key: string]: number } = {};
    let start: number = 0;
    let maxLength: number = 0;
    
    [...s].forEach((char: string, end: number) => {
        if (char in seen && seen[char] >= start) {
            start = seen[char] + 1;
        } else {
            maxLength = Math.max(maxLength, end - start + 1);
        }
        seen[char] = end;
    });
    
    return maxLength;
}