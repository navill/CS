def fibo_iter(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        current = 1; last = 0; temp = 0
        for _ in range(3, n+1):
            temp = current
            current += last
            last = temp
    
        return current

if __name__ == '__main__':
    for i in range(1, 11):
        print(fibo_iter(i), end = "  ")

