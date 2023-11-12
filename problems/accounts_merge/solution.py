from collections import defaultdict

class UnionFind:
    def __init__(self, n: int):
        self.rank = [0] * n
        self.parents = list(range(n))
    
    def find(self, node: int) -> int:
        parent = self.parents[node]

        while parent !=  self.parents[parent]:
            self.parents[parent] = self.parents[self.parents[parent]]
            parent = self.parents[parent]
        
        return parent
    
    def union(self, node1: int, node2: int) -> bool:
        parent1, parent2 = self.find(node1), self.find(node2)
        
        if parent1 == parent2:
            return False

        if self.rank[parent1] > self.rank[parent2]:
            self.parents[parent2] = parent1
        elif self.rank[parent1] < self.rank[parent2]:
            self.parents[parent1] = parent2
        else:
            self.parents[parent2] = parent1
            self.rank[parent1] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union_find = UnionFind(len(accounts))

        email_to_ind = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in email_to_ind:
                    union_find.union(email_to_ind[email], i)
                email_to_ind[email] = i
        
        result_dict = defaultdict(list)
        for email, ind in email_to_ind.items():
            i = union_find.find(ind)
            result_dict[i].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in result_dict.items()]
        