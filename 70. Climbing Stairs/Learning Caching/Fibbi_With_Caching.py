def recurse(cur):
    if cur in fibbi:
        return fibbi[cur]
    else:
        fibbi[cur] = recurse(cur-1) + recurse(cur-2)
        return fibbi[cur]

if __name__ == '__main__':
    fibbi = {}
    fibbi[0] = 0
    fibbi[1] = 1
    fibbi[2] = 1
    n = 10
    print(recurse(int(n)))
    print(fibbi)
