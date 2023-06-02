from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for _src, _dst, _price in flights:
            graph[_src].append((_dst, _price))
        
        if not graph[src]:
            return -1
        
        q, minPrice = deque([(src, 0)]), float("inf")
        prices = [float("inf")] * n

        k += 1

        while k >= 0 and q:
            _len = len(q)

            for _ in range(_len):
                node, price = q.popleft()

                if prices[node] <= price:
                    continue
                
                prices[node] = price

                if node == dst and minPrice > price:
                    minPrice = price

                for _node, _price in graph[node]:
                    q.append((_node, price + _price))         
            
            k -= 1
        
        return -1 if isinf(minPrice) else minPrice
