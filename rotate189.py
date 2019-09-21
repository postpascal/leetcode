class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k=k%len(nums)
        # nums[:]=nums[::-1]
        # nums[:k]=nums[:k][::-1]
        # nums[k:]=nums[k:][::-1]
        k=k%len(nums)

        for l,r in [(0,len(nums)-1),(0,k-1),(k,len(nums)-1)]:
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l=l+1
                r=r-1