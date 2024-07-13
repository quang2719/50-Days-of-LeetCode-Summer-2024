class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1,n+1)]
        res = 0
        next_step = (res+k-1)%n
        while(len(arr)>1):
            arr.remove(arr[next_step])
            next_step = (next_step+k-1)%len(arr)
        return arr[0]