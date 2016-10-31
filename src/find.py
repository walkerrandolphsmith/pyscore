def find(collection, predicate):
    for element in collection:
        if predicate(element):
            return element
    return None
