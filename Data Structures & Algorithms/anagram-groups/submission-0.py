class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #1 Idea is to hashmap with defaultdict[list]
        hashmap = defaultdict(list)

        for i in range (len(strs)):
            s = "".join(sorted(strs[i]))
            hashmap[s].append(strs[i])

        return list(hashmap.values())

        