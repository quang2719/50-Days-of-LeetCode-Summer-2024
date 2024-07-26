class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapping_num(num,mapping):
            num = str(num)
            res = 0
            for i in num:
                res = res*10 + mapping[int(i)]
            return res
        arr = []
        for i,num in enumerate(nums):
            map_val = mapping_num(num,mapping)
            newNum = MapNum(num,map_val,i)
            arr.append(newNum)
        arr.sort()
        return [x.num for x in arr]
class MapNum:
    def __init__(self, num, mapVal,order):
        self.num = num
        self.mapVal = mapVal
        self.order  = order
    def __lt__(self, other):
        if self.mapVal == other.mapVal:
            return self.order < other.order
        return self.mapVal < other.mapVal