def fibonacci_last_digit(n):
    first = 0
    second = 1

    for i in range(2, n+1, 1):
        res = (first + second) % 10
        first = second
        second = res

    return res

if __name__ == '__main__':

    n = input("Enter the nth number you want to caculate for fibonacci: ")
    print(fibonacci_last_digit(int(n)))
