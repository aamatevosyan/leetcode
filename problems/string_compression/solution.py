class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 0:
            return []

        result = []
        prev_char = chars[0]
        cnt = 1
        
        ind = 0

        for i in range(1, len(chars)):
            c = chars[i]

            if prev_char != c:
                chars[ind] = prev_char
                ind += 1

                if cnt > 1:
                    for n in str(cnt):
                        chars[ind] = n
                        ind += 1
                
                cnt = 1
            
            if c == prev_char:
                cnt += 1
            
            prev_char = c
        
        chars[ind] = prev_char
        ind += 1

        if cnt > 1:
            for n in str(cnt):
                chars[ind] = n
                ind += 1

        return ind