class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for x in details:
            age = int(x[11:13])
            if age>60: count+=1
        return count