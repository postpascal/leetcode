class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
        	for j in range(i, len(nums)):
        		if nums[i]+nums[j]==target:
        			return [i,j]
        return []

        

if __name__ == "__main__":
