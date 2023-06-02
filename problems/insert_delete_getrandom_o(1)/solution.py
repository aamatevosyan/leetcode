from random import randint

class RandomizedSet:

    def __init__(self):
        self.numbers = []
        self.indexes = {}
        

    def insert(self, val: int) -> bool:
        if val in self.indexes:
            return False
        
        self.indexes[val] = len(self.numbers)
        self.numbers.append(val)
        
        return True
        

    def remove(self, val: int) -> bool:
        if not val in self.indexes:
            return False
        
        to_delete_index, number_to_keep = self.indexes[val], self.numbers[-1]
        self.numbers[to_delete_index] = number_to_keep
        self.indexes[number_to_keep] = to_delete_index

        self.numbers.pop()
        self.indexes.pop(val)
        
        return True

        

    def getRandom(self) -> int:
        ind = randint(0, len(self.numbers) - 1)

        return self.numbers[ind]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()