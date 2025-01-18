"""This function merges two sorted arrays, nums1 and nums2, into a single sorted array within nums1, maintaining its
length by considering only the first m elements of nums1 and the entire nums2.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result
can fit in nums1."""


def merge(nums1, m, nums2, n):
    nums1_copy = nums1[:m]
    nums1.clear()
    i = 0
    j = 0
    while i < m and j < n:
        if nums1_copy[i] <= nums2[j]:
            nums1.append(nums1_copy[i])
            i += 1
        else:
            nums1.append(nums2[j])
            j += 1
    while i < m:
        nums1.append(nums1_copy[i])
        i += 1
    while j < n:
        nums1.append(nums2[j])
        j += 1
    print(nums1)


num1 = [1, 2, 3, 0, 0, 0]
g = 3
num2 = [2, 5, 6]
v = 3
merge(num1, g, num2, v)