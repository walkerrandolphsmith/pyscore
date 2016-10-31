def find_index(collection, predicate):
    i = 0
    for element in collection:
        if predicate(element):
            return i
        i += 1
    return -1
