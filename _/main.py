def compact(collection):
    return [element for element in collection if element]

def difference(collection, other_collection):
    return list(set(collection) - set(other_collection))

def every(collection, predicate):
    for e in collection:
        if not predicate(e):
            return False
    return True

def find_all(collection, predicate):
    new_list = []
    for element in collection:
        if predicate(element):
            new_list.append(element)
    return new_list

def find_index(collection, predicate):
    for i, element in enumerate(collection):
        if predicate(element):
            return i
    return -1

def find(collection, predicate):
    for element in collection:
        if predicate(element):
            return element
    return None

def group_by(collection):
    groups = {}
    for v, k in collection:
        groups[k] = groups[k] + [v] if k in groups else [v]
    return groups

def _interleave(*collections):
    iterators = [iter(collection) for collection in collections]
    while iterators:
        next_iterators = []
        for iterator in iterators:
            try:
                yield next(iterator)
                next_iterators.append(iterator)
            except StopIteration:
                pass

        iterators = next_iterators

def interleave(*collections):
    return list(_interleave(*collections))

def intersection(collection, other_collection):
    return list(set(collection).intersection(other_collection))

def partition(c, p):
    l1, l2 = [], []
    for e in c:
        l1.append(e) if p(e) else l2.append(e)
    return [l1, l2]

def pluck(c, property_name):
    l = []
    for e in c:
        l.append(e[property_name])
    return l

def reject(collection, predicate):
    l = []
    for e in collection:
        if not predicate(e):
            l.append(e)
    return l

def reverse(collection):
    return collection[::-1]

def some(c, p):
    for e in c:
        if p(e):
            return True
    return False

def union(collection, other_collection):
    return list(set(collection).union(other_collection))

def _unique(collection):
    seen = []
    for i, element in enumerate(collection):
        if element not in seen:
            seen.append(element)
            yield (i, element)

def unique(collection):
    return [collection[i] for i, _ in _unique(collection)]
