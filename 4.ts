function findMedianOfSortedArrays(nums1: number[], nums2: number[]): number {
    // Ensure nums1 is the smaller array
    if (nums1.length > nums2.length) {
        [nums1, nums2] = [nums2, nums1];
    }
    
    const m: number = nums1.length;
    const n: number = nums2.length;
    let low: number = 0;
    let high: number = m;
    
    while (low <= high) {
        const partitionX: number = Math.floor((low + high) / 2);
        const partitionY: number = Math.floor((m + n + 1) / 2) - partitionX;
        
        const maxLeftX: number = partitionX === 0 ? Number.NEGATIVE_INFINITY : nums1[partitionX - 1];
        const minRightX: number = partitionX === m ? Number.POSITIVE_INFINITY : nums1[partitionX];
        const maxLeftY: number = partitionY === 0 ? Number.NEGATIVE_INFINITY : nums2[partitionY - 1];
        const minRightY: number = partitionY === n ? Number.POSITIVE_INFINITY : nums2[partitionY];
        
        if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
            if ((m + n) % 2 === 0) {
                return (Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2;
            } else {
                return Math.max(maxLeftX, maxLeftY);
            }
        }
        else if (maxLeftX > minRightY) {
            high = partitionX - 1;
        }
        else {
            low = partitionX + 1;
        }
    }
    
    return 0; // Should never reach here if input arrays are sorted
}