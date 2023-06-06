class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        meet_character, current_len = 0, False

        for c in reversed(s):
            if c == ' ':
                if meet_character:
                    break
                
                continue

            meet_character = True
            current_len += 1
        
        return current_len
            
