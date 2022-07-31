def fibonacci_naive (n):
    if (n <= 1):
        return n
    else:
        return (fibonacci_naive(n-1) + fibonacci_naive(n-2))

def fibonacci_fast(n):
    f = []
    f.insert(0, 0)
    f.insert(1, 1)

    for i in range(2, n+1, 1):
        f.insert(i, (f[i-1] + f[i-2]))

    return f[n]


if __name__ == '__main__':
    
    n = int(input("Enter the fibonacci you want to know:"))
    print(fibonacci_naive(n))
    print(fibonacci_fast(n))