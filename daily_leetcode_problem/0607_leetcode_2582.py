class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        loop = time//(n-1)
        residual = time%(n-1)
        return (residual+1) if loop %2==0 else(n-residual)

