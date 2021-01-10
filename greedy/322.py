class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return amount
        
        coins.sort() 
        counter = 0
        while amount!=0:
            if not coins:
                return -1
            dif = amount - coins[-1]
            if dif >= 0:
                counter += 1
                amount -= coins[-1]
            elif dif < 0:
                coins.pop()

                
        return counter
            
        