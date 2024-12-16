#include <limits.h>
#include <math.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    // Ensure nums1 is the smaller array
    if (nums1Size > nums2Size) {
        int* temp = nums1;
        nums1 = nums2;
        nums2 = temp;
        int tempSize = nums1Size;
        nums1Size = nums2Size;
        nums2Size = tempSize;
    }
    
    int low = 0;
    int high = nums1Size;
    int m = nums1Size;
    int n = nums2Size;
    
    while (low <= high) {
        int partitionX = (low + high) / 2;
        int partitionY = (m + n + 1) / 2 - partitionX;
        
        int maxLeftX = (partitionX == 0) ? INT_MIN : nums1[partitionX - 1];
        int minRightX = (partitionX == m) ? INT_MAX : nums1[partitionX];
        int maxLeftY = (partitionY == 0) ? INT_MIN : nums2[partitionY - 1];
        int minRightY = (partitionY == n) ? INT_MAX : nums2[partitionY];
        
        if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
            if ((m + n) % 2 == 0) {
                return (fmax(maxLeftX, maxLeftY) + fmin(minRightX, minRightY)) / 2.0;
            } else {
                return fmax(maxLeftX, maxLeftY);
            }
        }
        else if (maxLeftX > minRightY) {
            high = partitionX - 1;
        }
        else {
            low = partitionX + 1;
        }
    }
    
    return 0.0;
}