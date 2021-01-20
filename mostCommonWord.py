class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_count = defaultdict(int)
        # word_count = {}
        newString = paragraph.lower()
        for c in string.punctuation:
            newString = newString.replace(c, " ")

        words = newString.split()
        for word in words:
            if word not in banned:
                word_count[word] += 1
#             else:
#                 word_count[word] = 1

        return max(word_count.items(), key=operator.itemgetter(1))[0]

# Time Complexity: O(N) - Iterate through each word
# Space Complexity: O(N) - Space for hashmaps with words
# Videos: https://www.youtube.com/watch?v=xwwYAP_Y4PA
