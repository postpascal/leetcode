class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def quick(l,r,k):
            low=l
            high=r
            kk=nums[l]
            if l>=r:
                return nums[l]

            while l<r:
                while l<r and nums[r]<kk:
                    r-=1
                nums[l]=nums[r]
                while l<r and nums[l]>=kk:
                    l+=1
                nums[r]=nums[l]
            nums[l]=kk
            if l==k:
                return nums[l]
            elif l<k:
                return quick(r+1,high,k)
            else:
                return quick(low,l-1,k)

        k=k-1
        return quick(0,len(nums)-1,k)


a=Solution()
print(a.findKthLargest([3,2,3,1,2,4,5,5,6],4))