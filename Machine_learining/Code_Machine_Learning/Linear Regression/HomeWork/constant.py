TRAINING_SET = ((0,1),(1,3),(2,5),(3,7))
import random

def random_point(k=10):
    import random
    list = []
    for i in range(0,k):
        a = random.randint(0,10)
        b = random.randint(0,100)
        c = 3*a + b + 4
        list.append([a,b,c])
    return list

# list = random_point(10)
# for (key, item) in enumerate(list, start = 1):
#     print(key, '. ' ,item)
TRAINING_SET = ((0,1),(1,3),(2,5),(3,7))
