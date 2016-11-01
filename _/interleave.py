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