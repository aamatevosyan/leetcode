class Solution:
    START_NODE = "0000"

    def comibnations(self, node: str):
        for i in range(len(node)):
            digit = int(node[i])

            for delta in (-1, 1):
                next_digit = (digit + delta) % 10

                yield node[:i] + str(next_digit) + node[i + 1:]
    
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        level, q1, q2 = 0, set([self.START_NODE]), set([target])

        while q1 and q2:
            q = set()
            if len(q1) > len(q2):
                q1, q2 = q2, q1

            for node in q1:
                if node in dead:
                    continue
                
                if node in q2:
                    return level
                
                dead.add(node)
                for comibnation in self.comibnations(node):
                    q.add(comibnation)

            level += 1
            q1 = q2
            q2 = q
        
        return -1

        