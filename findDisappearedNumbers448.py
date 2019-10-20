class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i=0
        while i<len(nums):
            while nums[i]-1 !=i and nums[i]!=0:

                if nums[nums[i]-1]!=nums[i]:
                    nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
                else:
                    nums[i]=0
                    break
            i=i+1
            
        r=[]
        for j in range(len(nums)):
            if nums[j]==0:
                r.append(j+1)
        return r