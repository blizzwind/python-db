n = 1

def exc(d, q):
    global n
    if q.startswith("add"):
        q = q.split()
        if len(q) != 2 and q[0] != "add":
            return "error"
        try:
            d[str(n)] = q[1]
        except:
            return "error"
        n = n + 1
        return "added"
    elif q.startswith("query"):
        q = q.split()
        if len(q) != 2 and q[0] != "query":
            return "error"
        k = list(d.keys())
        v = list(d.values())
        try:
            p = v.index(q[1])
        except:
            return "error"
        return k[p]
    else:
        return "error"
