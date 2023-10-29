class Solution:
    START_NODE = "0000"

    def neighbors(self, node: str):
        for i in range(len(node)):
            digit = int(node[i])

            for delta in (-1, 1):
                next_digit = (digit + delta) % 10

                yield node[:i] + str(next_digit) + node[i + 1:]
    
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        level, begin, end = 0, set([self.START_NODE]), set([target])

        while begin and end:
            neighbors = set()
            for node in begin:
                if node in dead:
                    continue
                
                if node in end:
                    return level
                
                dead.add(node)
                for neighbor in self.neighbors(node):
                    neighbors.add(neighbor)

            level += 1
            begin = end
            end = neighbors
        
        return -1

        