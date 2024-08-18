from queue import PriorityQueue
class Solution:
    def minimumPushes(self, word: str) -> int:
        num_of_valid_key = 8
        dic = {}
        keys = []
        for x in word:
            dic[x] = dic.get(x,0)+1
        for x in dic:
            keys.append(key(x,dic[x]))
        keys.sort()
        res = 0
        press = 1
        for i in keys:
            if num_of_valid_key ==0:
                num_of_valid_key = 8
                press +=1
            res += i.seq*press
            num_of_valid_key-=1
        return res


class key():
    def __init__(self,val,seq):
        self.val = val
        self.seq = seq
    def __lt__(self,other):
        return self.seq >= other.seq
    
