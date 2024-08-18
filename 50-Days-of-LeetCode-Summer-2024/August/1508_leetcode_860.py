class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money_in_hand = {
            5:0,
            10:0
        }
        for x in bills:
            if x ==5:
                money_in_hand[5] +=5
            elif x==10:
                if money_in_hand[5]<5:
                    return False
                money_in_hand[5] -=5
                money_in_hand[10] += 10
            else:
                if money_in_hand[5] < 5:
                    return False
                if money_in_hand[10] < 10:
                    if money_in_hand[5] < 15:
                        return False
                    else:
                        money_in_hand[5] -= 15
                else:
                    money_in_hand[5] -=5
                    money_in_hand[10] -= 10
        return True