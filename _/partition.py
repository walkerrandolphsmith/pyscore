def partition(c, p):
    l1, l2 = [], []
    for e in c:
        l1.append(e) if p(e) else l2.append(e)
    return [l1, l2]
