class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_count = Counter(nums)
        heap = []

        for key, value in nums_count.items():
            heapq.heappush(heap,(-value,key))
            
        result=[]

        i = 0
        while i < k:
            num,key = (heapq.heappop(heap))
            result.append(key)
            i+=1
        return result

        

        

        

        
        





       

        