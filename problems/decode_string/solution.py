from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        cnt, st, result = 0, deque(), ''

        for c in s:
            if c.isdigit():
                cnt = cnt * 10 + int(c)
            elif c == '[':
                st.append((cnt, result))
                cnt, result = 0, ''
            elif c == ']':
                prev_cnt, prev_result = st.pop()
                result = prev_result + prev_cnt * result
            else:
                result += c
        
        return result
