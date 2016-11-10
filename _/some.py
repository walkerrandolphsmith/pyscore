def some(c, p):
    for e in c:
        if p(e):
            return True
    return False
