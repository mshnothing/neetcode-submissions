class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq={}

        for num in nums:
            frq[num]=frq.get(num,0)+1
        
        sort1=sorted([(k,v) for k,v in frq.items()],key=lambda x:x[1],reverse=True)

        return [x[0] for x in sort1[:k]]
