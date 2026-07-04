if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    my_set = set(arr)
    my_set = sorted(my_set)
    print(my_set[-2])