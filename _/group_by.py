def group_by(collection):
    groups = {}
    for v, k in collection:
        groups[k] = groups[k] + [v] if k in groups else [v]
    return groups