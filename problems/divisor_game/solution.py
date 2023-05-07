class Solution:        
    def divisorGame(self, n: int) -> bool:
        alice_turn = True
        current_number = 1
        
        while True:
            while n % current_number != 0 and current_number < n:
                current_number += 1
                
            if current_number >= n:
                break
            
            alice_turn = not alice_turn
            n = n - current_number
        
        return not alice_turn 
        