def vote(votes):
    d = {}
    for i in votes:
        d[i] = d.get(i, 0) + 1
    return max(d, key=d.get)

if __name__ == '__main__':
    print(vote([1,1,1,2,3]))
    print(vote([1,2,3,2,2]))
