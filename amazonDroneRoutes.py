def drone(forward, backward, maximum):

    i = 0
    j = len(backward)-1

    while i < len(forward) and j >= 0:
        if forward[i] + backward[j] == maximum:
            return i, j

        elif forward[i] + backward[j] > maximum:
            j -= 1

        # elif forward[i] + backward[j] < maximum:
        #     i+=1

        else:
            i += 1

    return -1, -1
