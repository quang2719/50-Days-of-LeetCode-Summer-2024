class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num_list = []
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0) +1
        for num in dic:
            new_num = number(num,dic[num])
            num_list.append(new_num)
        num_list.sort()
        return [num.num for num in num_list for _ in range(num.fre)]
class number:
    def __init__(self, num, fre):
        self.num = num
        self.fre = fre
    def __lt__(self, other):
        if self.fre == other.fre:
            return self.num > other.num
        return self.fre < other.fre
