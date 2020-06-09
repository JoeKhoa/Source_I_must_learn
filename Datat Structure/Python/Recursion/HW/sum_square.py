# 4.1
def sum_square(n):
    if n == 0:
        return 0
    if n == 1 :
        return 1
    else:
        return sum_square(n-1)+n**2
# n = 3
# x = sum_square(n)
# print(f'sum_square of {n} is : {x}')


def sum(n):
    if n == 0: return 0
    return sum(n-1)+n

# n = 3
# print(f'sum_square of {n} is : {sum(n)}')

def max_in_array(n, array):
    if n == 1:
        return array[0]
    else:
        if array[n-1] > array[n-2]:
            array[n-2] = array[n-1]
            print(array)
        return max_in_array(n-1,array)

a = [1,2,4,2,124,50]
n = 5
print(f'max of {n} first element is : {max_in_array(n,a)}')
