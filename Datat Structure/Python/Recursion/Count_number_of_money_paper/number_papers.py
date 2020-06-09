
def So_to( Amount, size, A):
    n = Amount//A[size-1]
    k = Amount % A[size-1]
    if k == 0:
        return n
    else:
        for i in range (size-2, -1, -1):
            if not(k%A[i]):
                return n+1
            else:
                return n+So_to(k%A[i],size-2,A)
    return 0


A = (6,7,11)
Amount_A = 57
size_A = len(A)

x = So_to(Amount_A, size_A, A)
print(x)
print(A[0])
# for i in range(len(A)-1,-1,-1):
#     print(A[i])
