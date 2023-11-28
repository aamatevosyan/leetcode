class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []

        for asteroid in asteroids:
            while result and asteroid < 0 and result[-1] > 0:
                if result[-1] + asteroid == 0:
                    result.pop()
                    break
                elif result[-1] + asteroid > 0:
                    break
                else:
                    result.pop()
                    continue
            else:
                result.append(asteroid)
        
        return result
        