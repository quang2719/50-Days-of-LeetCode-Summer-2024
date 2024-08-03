class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_1_number = sum(nums)
        window = sum(nums[:total_1_number])
        res = total_1_number - window
        for i in range(1,len(nums)):
            end_window = i+total_1_number -1
            if end_window >= len(nums):
                end_window -= len(nums)
            if nums[i-1] == 1: window -=1
            if nums[end_window] == 1: window +=1
            res = min(res,total_1_number-window)
        return res