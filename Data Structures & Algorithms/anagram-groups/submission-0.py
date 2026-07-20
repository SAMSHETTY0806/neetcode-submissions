class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag= {}
    
        for word in strs:
            sorted_key = "".join(sorted(word))
            anag.setdefault(sorted_key, []).append(word)
        return list(anag.values())
        