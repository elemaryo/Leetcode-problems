'''final task
From string s, find all the substrings of size k with exactly (k-1) unique characters.
Print the index of the valid substrings

Input
s = "iraceacar"
k = 5

Expected output
[1, 4]

'''

'''task 1 count chars a str, return a dict'''


def substrings(s, k):

    characters = {}
    result = []

    # first window
    for i in range(k):
        if s[i] in characters:
            characters[s[i]] += 1

        else:
            characters[s[i]] = 1

        if len(characters) == k - 1:
            result.append(0)  # i, i+k-1


'''task 2 apply sliding window to the dictionary.
    Delete the leaving character, add the joining character to dict every time the window slides.
'''

for i in range(1, len(s) - k):
        # window = window - s[i-1] + s[i+k-1]
        characters[s[i-1]] -= 1

        if characters[s[i-1]] == 0:
            characters.pop(s[i-1])

        if s[i] in characters:
            characters[s[i]] += 1

        else:
            characters[s[i]] = 1

        if len(characters) == k - 1:
            result.append(i)  # i, i+k-1
