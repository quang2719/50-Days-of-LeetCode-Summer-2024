class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic = {}
        for i in arr: dic[i] = dic.get(i,0) +1
        count = 0
        for i in dic.keys():
            if dic[i]==1:
                count+=1
                if count==k: return i
        return ""
         