class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        c=0
        n1=len(nums1)
        n2=len(nums2)
        for i in range(n1):
            for j in range(n2):
                if nums1[i] % ( nums2[j] *k ) ==0:
                    c = c+1
        return c 