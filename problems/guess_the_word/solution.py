# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def compare(self, a: List[str], b: List[str]) -> int:
        result = 0

        for _a, _b in zip(a, b):
            if _a == _b:
                result += 1

        return result

    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        sortedWords = sorted(words, key=lambda x: len(set(x)))
        used = []

        while sortedWords:
            curr = sortedWords.pop()
            matched = master.guess(curr)

            if matched == 6:
                return

            sortedWords = [
                word
                for word in sortedWords
                if self.compare(word, curr) == matched
            ]


