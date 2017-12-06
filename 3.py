def untouchable_function(n):
    if n == 0:
        return
    untouchable_function(n - 1)

if __name__ == '__main__':
    for i in range(101):
        untouchable_function(i)
        print(i)
