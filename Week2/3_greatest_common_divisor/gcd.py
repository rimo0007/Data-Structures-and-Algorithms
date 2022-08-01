def gcd_naive(a, b):

    if b == 0:
        return abs(a)
    else:
        return (gcd_naive(b, a % b))

# method to compute gcd ( Euclidean algo )
def computeGCD(x, y):
    while(y):
        x, y = y, x % y
    return abs(x)

def computerGCDLoop(a, b):
    if a < b:
        small = a
    else:
        small =b
    for i in range(1, small + 1):
        if (a % i ==0 and b % i == 0):
            gcd = i
    return gcd

    
if __name__ == '__main__':

    a = int(input("Enter the first number you want to calculate GCD: "))
    b = int(input("Enter the second number you want to calculate GCD: "))

    print ("The gcd is: ", gcd_naive(a, b))
    print ("The gcd using Euclidean: ", computeGCD(a, b))
    print ("The gcd using Loop: ", computeGCD(a, b))

