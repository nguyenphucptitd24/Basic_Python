if __name__ == '__main__':
    N = int(input())
    lists = []
    for _ in range (N):
        line = input().split()
        s = line[0]
        if s == "insert":
            i = int(line[1])
            v = int(line[2])
            lists.insert(i, v)
        elif s == "remove":
            u = int(line[1])
            lists.remove(u)
        elif s == "append":
            u = int(line[1])
            lists.append(u)
        elif s == "sort":
            lists.sort()
        elif s == "pop":
            lists.pop()
        elif s == "reverse":
            lists.reverse()
        elif s == "print":
            print(lists)
        
            
            