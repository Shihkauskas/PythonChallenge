def untouch_decorator(function):
    def iterations(num):
        print(num)
        function(num)
    return iterations


@untouch_decorator
def untouchable_function(n):
    if n == 0:
        return
    untouchable_function(n - 1)


if __name__ == '__main__':
    untouchable_function(100)
