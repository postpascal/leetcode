class Solution:
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False
        base = nums[0]
        lid = None
        lastLid = None
        for index in range(1, len(nums)):
            if nums[index] > base:
                if lastLid != None and nums[index] > lastLid:
                    return True
                if lid == None:
                    lid = nums[index]
                elif nums[index] > lid:
                    return True
                elif nums[index] < lid:
                    lid = nums[index]
            else:
                if lid != None:
                    lastLid = lid
                base = nums[index]
                lid = None