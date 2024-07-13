class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        total_waiting = 0
        finished_time = 0
        finished_time = (customers[0][0] + customers[0][1]) 
        total_waiting += finished_time - customers[0][0]
        for i in range(1,n):
            start = max(customers[i][0],finished_time)
            finished_time = (start + customers[i][1]) 
            total_waiting += finished_time - customers[i][0]
        return total_waiting/n
