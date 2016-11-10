def reject(collection, predicate):
    l = []
    for e in collection:
        if not predicate(e):
            l.append(e)
    return l
