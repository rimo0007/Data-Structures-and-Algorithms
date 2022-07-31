def MaxPairWiseProduct(numbers):
    size = len(numbers)
    
    max_product = 0

    for first in range(0, size, 1) :
        for second in range(first + 1, size, 1):
            if (numbers[first] * numbers[second]) > max_product:
                max_product = numbers[first] * numbers[second]

    return max_product

def MaxPairWiseProductFast(numbers):
    size = len(numbers)
    max_index1 = -1

    for first in range(0, size, 1):
        if ((max_index1 == -1) or (numbers[first] > numbers[max_index1])):
            max_index1 = i
    
    max_index2 = 0
    for second in range(0, size, 1):
        if (((max_index2 == 0-1) or (numbers[second] > numbers[max_index2])) and  (second != max_index1)):
            max_index2 = second
    
    #print("Max Index: ", max_index1)
   # print("Second Max Index", max_index2)

    return (numbers[max_index1] * numbers[max_index2])



if __name__ == '__main__':

   x = int(input("Enter the length: "))
   numbers = []
   print("Enter the numbers: ")
   for i in range(0, x):
    l = int(input())
    numbers.append(l)
    
print("Result:" ,MaxPairWiseProductFast(numbers=numbers))
