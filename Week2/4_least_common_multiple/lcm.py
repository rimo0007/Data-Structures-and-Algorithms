def euclidGCD(a, b):
    if b==0:
        return a
    else:
        return euclidGCD(b, a%b)

def lcm_naive(a, b):

    return int((a*b) /euclidGCD(a, b))

if __name__ == '__main__':
    
    print("Enter the numbers you want to calculate LCM: ")
    a = int(input())
    b = int(input())

    print("The LCM is: ", lcm_naive(a, b))

