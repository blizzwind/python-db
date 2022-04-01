n = 1

def exc(d, q):
    global n
    t = []
    if q.startswith("add"):
        q = q.split(" ")
        if len(q) != 2 or q[0] != "add":
            return "error"
        else:
            try:
                d[str(n)] = q[1]
            except:
                return "error"
            n = n + 1
            return "added"
    elif q.startswith("query"):
        q = q.split(" ")
        if len(q) != 2 or q[0] != "query":
            return "error"
        else:
            try:
                for key, value in d.items():
                    if q[1] == value:
                        t.append(key)
            except:
                return "error"
            return t
    else:
        return "error"
