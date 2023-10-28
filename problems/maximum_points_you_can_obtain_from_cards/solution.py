class Solution:
    # 5 4 -1 4 | 2 -2 1 6
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        len_diff = len(cardPoints) - k
        curr_score = sum(cardPoints[len_diff:])
        max_score = curr_score

        for i in range(k):
            curr_score += cardPoints[i]
            curr_score -= cardPoints[len_diff + i]
            
            max_score = max(max_score, curr_score)

        return max_score
        