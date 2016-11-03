def _unique(collection):
    seen = []
    for i, element in enumerate(collection):
        if element not in seen:
            seen.append(element)
            yield (i, element)


def unique(collection):
    return [collection[i] for i, _ in _unique(collection)]
