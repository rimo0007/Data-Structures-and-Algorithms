def sum_of_two_digits(a, b):
    return a + b

if __name__ == '__main__':
    a, b = map(int, input("Enter two numbers using space  ").split())
    print(sum_of_two_digits(a, b))
