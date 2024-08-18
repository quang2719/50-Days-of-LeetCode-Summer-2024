from queue import PriorityQueue
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10**9+7
        cache = {}
        sum_arr = PriorityQueue()
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i==j:
                    sum_arr.put(nums[i])
                    cache[(i,j)] = nums[i]
                else:
                    sum_arr.put((cache[(i,j-1)]+nums[j])%mod)
                    cache[(i,j)] = (cache[(i,j-1)]+nums[j]) %mod

        res = 0
        for i in range(1,left):
            sum_arr.get()
        for i in range(left,right+1):
            res = (res+sum_arr.get())%mod
        return int(res)