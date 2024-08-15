class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1=set(sorted(nums1))
        nums2=set(sorted(nums2))
        q= [y-x for x, y in zip(sorted(nums1), sorted(nums2))]
        return q[0]