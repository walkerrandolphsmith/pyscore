def find_index(collection, predicate):
    for i, element in enumerate(collection):
        if predicate(element):
            return i
    return -1
