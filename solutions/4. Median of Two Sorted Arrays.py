def merge_sorted_arrays(nums1, nums2):
    nums1_len = len(nums1)
    nums2_len = len(nums2)
    nums3 = []
​
    i, j = 0, 0
​
    while i < nums1_len and j < nums2_len:
        if nums1[i] < nums2[j]:
            nums3.append(nums1[i])
            i = i + 1
        else:
            nums3.append(nums2[j])
            j = j + 1
    
    while i < nums1_len:
        nums3.append(nums1[i])
        i = i + 1
    
    while j < nums2_len:
        nums3.append(nums2[j])
        j = j + 1
​
    return nums3
​
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)
        nums3_len = len(nums3)
​
        if nums3_len % 2 == 0:
            slice1 = nums3[:nums3_len // 2]
            slice2 = nums3[nums3_len // 2:]
            return float(f"{(slice1[-1] + slice2[0]) / 2:.5f}")
        return float(f"{nums3[nums3_len // 2]:.5f}")
