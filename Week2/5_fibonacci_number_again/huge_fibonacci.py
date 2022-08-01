def  get_pisano_period(m):
    # 011 
    previous, current = 0, 1

    for i in range(0, m*m):
        previous, current = current, (previous + current) % m

        if (previous == 0 and current ==1):
            return i+1

def fibonacciModulo(n, m):
    
    pisano_period = get_pisano_period(m)
    n = n % pisano_period
    previous, current = 0, 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    for i in range(0, n-1):
        previous, current \
        = current, previous + current
    
    return (current % m)



if __name__ == '__main__':
    
    print("Enter value of n: ")
    n = int(input())

    print("Enter value of m: ")
    m = int(input())

    print(fibonacciModulo(n, m))


