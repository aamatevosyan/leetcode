from collections import deque

class Solution:
    def reverseWords(self, s: str) -> str:
        st = deque()

        for word in s.split(" "):
            if word:
                st.appendleft(word)

        return " ".join(st)