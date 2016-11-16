def without(l, *values):
    for v in values:
        if v in l:
            l.remove(v)
    return l
