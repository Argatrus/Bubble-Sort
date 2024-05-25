def bubble_sort(l: list):
    while True:
        sorted = True
        for f, i in enumerate(l):
            if f+1 < len(l):
                if i > l[f+1]:
                    sorted = False
                    l[f+1], l[f] = i, l[f+1]
        if sorted:
            break
    return l

