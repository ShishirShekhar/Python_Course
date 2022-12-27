if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    temp = list(set(arr))
    print(temp[-2])
