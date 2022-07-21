class Solution:
    def get_difference(self, n):
        return {n - i for i in self.coins if n - i >= 0}
      
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        amount_queue = {amount}
        checked = set()
        count = 0
        while amount_queue and 0 not in amount_queue:
            temp_amount = set()
            for amount in amount_queue:
                if amount not in checked:
                    checked.add(amount)
                    temp_amount |= self.get_difference(amount)
            amount_queue = temp_amount
            count += 1
        return count if 0 in amount_queue else -1
            
        
        
        '''
        11 -> 10 9 6
        6 -> 5 4 1 ; 9 -> 8 7 4 ; 10 -> 9 8 5
        1 -> 0 _ _ ; 4 -> 3 2 _ ; 5 -> 4 3 0 ; 8 -> 7 6 3; 7 -> 6 5 2 ; 9 -> 
        
        '''
