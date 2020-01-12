class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = strs
        # Initalizes an empty result dictionary where {key: []}
        result = collections.defaultdict(list)
        
        # take the word, sort it and turn the sorted word int a tuple as the key
        for word in s:
            result[tuple(sorted(word))].append(word)
            
        return result.values()
        
#     # Initalizes an empty result dictionary where {key: []}
#         result = collections.defaultdict(list)
#     # Initalize array of hash that has number of letter occurances
#         # [['e': 1, 'a': 1, 't': 1]]
#         counterOfOccurances = []
        
#         for word in s:
#             if collections.Counter(word) in counterOfOccurances:
#                 # returns the index of the collection counter array
#                 key = counterOfOccurances.index(collections.Counter(word))
#                 result[key].append(word)
            
#             else:
#                 counterOfOccurances.append(collections.Counter(word))             
#                 result[len(counterOfOccurances)-1].append(word)
                
#         return result.values()