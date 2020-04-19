def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores.sort()
    listLength = 3 if len(scores) >= 3 else len(scores)
    newA = []
    i = len(scores) - 1
    while listLength > 0:
        newA.append(scores[i])
        i -= 1
        listLength -= 1

    return newA
