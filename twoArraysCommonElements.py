a = [1, 1, 1, 2, 2, 2, 3]
b = [1, 2, 2, 2, 2, 4]
result = []

i = 0
j = 0

while i < len(a) and j < len(b):
    if a[i] == b[j]:
        result.append(a[i])
        i += 1
        j += 1

    elif a[i] > b[j]:
        j += 1

    else:
        i += 1


while i < len(a):
    i += 1

while j < len(b):
    j += 1
