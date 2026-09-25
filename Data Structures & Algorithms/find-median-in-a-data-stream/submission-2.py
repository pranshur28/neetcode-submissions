class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        if len(self.arr) == 0:
            self.arr.append(num)
            return
        i = 0 
        while i < len(self.arr) and self.arr[i] < num:
            i += 1
        self.arr.insert(i,num)

    def findMedian(self) -> float:
        n = len(self.arr)
        mid = n // 2

        if n%2 == 1:
            return float(self.arr[mid])

        left = self.arr[mid - 1]
        right = self.arr[mid]
        return (left + right) / 2.0
        
        