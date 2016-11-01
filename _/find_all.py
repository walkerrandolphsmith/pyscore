def find_all(collection, predicate):
    new_list = []
    for element in collection:
        if predicate(element):
            new_list.append(element)
    return new_list
