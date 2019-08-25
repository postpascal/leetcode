# class LargerNumKey(str):
#     def __lt__(x, y):
#         return x+y > y+x
        
# class Solution:
#     def largestNumber(self, nums):
#         largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
#         return '0' if largest_num[0] == '0' else largest_num

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums=list(map(str,nums))

        def quick(l,r):
            low=l
            hi=r
            if l>=r:
                return 
            k=nums[l]
            while l<r:
                while k+nums[r]>=nums[r]+k and l<r:
                    r-=1
                nums[l]=nums[r]
                while nums[l]+k>=k+nums[l] and l<r:
                    l+=1
                nums[r]=nums[l]
            nums[r]=k
            quick(low,l-1)
            quick(r+1,hi)

        quick(0,len(nums)-1)
        
        return str(int("".join(nums)))


a=Solution()
print(a.largestNumber([1,1,1]))