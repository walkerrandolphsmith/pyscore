def every(collection, predicate):
    for e in collection:
        if not predicate(e):
            return False
    return True
