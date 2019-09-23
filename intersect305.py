class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
    
        ans = []
        my_dict = {}

        for i in range(len(nums1)):
            if nums1[i] not in my_dict:
                my_dict[nums1[i]] = 0
            my_dict[nums1[i]] += 1

        for j in range(len(nums2)):
            if nums2[j] not in my_dict:
                continue
            if my_dict[nums2[j]] > 0:
                ans.append(nums2[j])
                my_dict[nums2[j]] -= 1

        return ans