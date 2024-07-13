class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = numBottles
        while numBottles >= numExchange:
            newBottles = numBottles//numExchange
            count+= newBottles
            numBottles = numBottles%numExchange + newBottles
        return count