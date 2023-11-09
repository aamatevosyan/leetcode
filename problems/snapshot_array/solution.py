from bisect import bisect_right

class SnapshotArray:

    def __init__(self, length: int):
        self.length = length

        self.store = [[(-1, 0)] for _ in range(length)]
        self.current_snap = 0

    def set(self, index: int, val: int) -> None:
        if self.store[index][-1][0] == self.current_snap:
            self.store[index][-1] = (self.current_snap, val)
        else:
            self.store[index].append((self.current_snap, val))
        

    def snap(self) -> int:
        self.current_snap += 1

        return self.current_snap - 1
        

    def get(self, index: int, snap_id: int) -> int:
        i = bisect_right(
                self.store[index], (snap_id + 1, 0), lo=0, hi=len(self.store[index])
            ) - 1

        return self.store[index][i][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)