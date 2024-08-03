class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        dic1 = {}
        dic2 = {}
        for x in arr: dic1[x] = dic1.get(x,0)+1
        for x in target: dic2[x] = dic2.get(x,0)+1
        for x in dic1:
            if x not in dic2 or dic1[x] != dic2[x]:
                return False
        return True