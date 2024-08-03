class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i,rate_i in enumerate(rating):
            l_less, l_greater, r_less, r_greater = 0,0,0,0
            for rate_j in rating[:i]:
                if rate_j < rate_i:
                    l_less+=1
                else: l_greater +=1
            for rate_j in rating[(i+1):]:
                if rate_j < rate_i:
                    r_less += 1
                else: r_greater +=1
            count += ((l_less*r_greater) + (l_greater*r_less))
        return count