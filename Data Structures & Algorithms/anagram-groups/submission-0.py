class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output={}
        for item in strs:
            sort1="".join(sorted(item))
            output[sort1]=output.get(sort1,[])+[item]
        return list(output.values())
                
        