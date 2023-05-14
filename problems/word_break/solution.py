from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque([s])
        visited = set([s])

        while q:
            word = q.popleft()

            for w in wordDict:
                if word.startswith(w):
                    newWord = word[len(w):]
                    if not newWord:
                        return True

                    if newWord not in visited:
                        q.append(newWord)
                        visited.add(newWord)
        
        return False
