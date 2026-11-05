class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map={}
        out_Put=[]

        for num in tuple(nums):
            hash_map[num]=1+hash_map.get(num,0)
            # hash_map[num]=0
        unique=list(hash_map)
        # for num in nums:
        #     hash_map[num]+=1
        sorted_dict =  sorted(hash_map, key=hash_map.get, reverse=True)
        return sorted_dict[:k]