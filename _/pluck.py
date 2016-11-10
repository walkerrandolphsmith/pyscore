def pluck(c, property_name):
    l = []
    for e in c:
        l.append(e[property_name])
    return l
