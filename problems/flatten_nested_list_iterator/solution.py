# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    @classmethod
    def get(cls, currList: List[NestedInteger]) -> Iterator[int]:
        for nestedInteger in currList:
            if nestedInteger.isInteger():
                yield nestedInteger.getInteger()
            else:
                yield from cls.get(nestedInteger.getList())

    def __init__(self, nestedList: [NestedInteger]):
        self.generator = self.get(nestedList)
        self.nextInteger = next(self.generator, None)
    
    def next(self) -> int:
        result = self.nextInteger
        self.nextInteger = next(self.generator, None)

        return result
    
    def hasNext(self) -> bool:
         return self.nextInteger is not None 

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())