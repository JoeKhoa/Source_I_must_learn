# from constant import *
TRAINING_SET = ((0,1),(1,3),(2,5),(3,7))

def Hypothesis(theta_list, row_key):
    Hypo = 0
    # not list (theta0, theta_1,..., y) remove y from list
    print('row_key', row_key)
    print('theta_list', theta_list)
    for theta_key in range(0, len(theta_list)):
        if theta_key == 0:
            Hypo = theta_list[theta_key]
        else:
                # index          0  1  2
                # theta         t0 t1 t2
                # train_set  x0 x1 x2 y
            Hypo += theta_list[theta_key]*TRAINING_SET[row_key][theta_key-1]
    print('Hypo',Hypo)
    return Hypo

def product_sum(theta_list, key): # for every training_set_row = m(i)
    sum = 0
    for (row_key, row_val) in enumerate(TRAINING_SET):
        y = row_val[-1]
        if key == 0:
            sum += (Hypothesis(theta_list, row_key) - y )
        else: # loss*x[i]
            sum += (Hypothesis(theta_list, row_key) - y )*row_val[key]
        print('sum:', sum)
    return sum


def Cost_(theta_list):
    cost = 0
    for (key_row, val) in enumerate(TRAINING_SET):
        cost += (Hypothesis(theta_list, key_row) - val[-1])**2
    return cost

def linear_regression():
    m = len(TRAINING_SET)
    n = len(TRAINING_SET[0])-1 #() [theta0, theta_1,..., y] remove y from list
    theta_list = [0]*(n+1)
    alpha = 0.1
    cost = 1000
    count = 0
    stop = 5
    # print(theta_list)
    while cost > 0.00000001 and count < stop:
    # while cost > 0.001:
        # get OLD theta list
        list_k1n = theta_list
        # calculate variable Theta
        for key in range(0,n):
            theta_list[key] = list_k1n[key] - alpha*(1/m)*product_sum(list_k1n,key)
        cost = Cost_(theta_list)
        count = count + 1
    # return {'theta list' : theta_list,
    #         'cost':cost, 'count':count}
    return { 'cost':cost}
# for k,v in linear_regression().items():
#     if k == 'theta_list':
#         for i,j in v.items():
#             print(i,':', j)
    print(k,':', v)

print(linear_regression())
