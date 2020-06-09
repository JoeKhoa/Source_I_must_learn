from constant import *

def Hypothesis(theta__0, theta__1, x):
    return theta__0 + theta__1*x

def product_sum(theta0, theta1, k=0):
    sum = 0
    for i in TRAINING_SET:
        x = i[0]
        y = i[1]
        m = 1 if k == 0 else x
        sum = sum + ( Hypothesis(theta0,theta1,x) - y )*m
    return sum


def Cost_(theta0, theta1):
    cost = 0
    for i in TRAINING_SET:
        x = i[0]
        y = i[1]
        cost = cost + ( Hypothesis(theta0, theta1, x) - y )**2
    return cost

def linear_regression():
    TRAINING_SET = ((0,1),(1,3),(2,5),(3,7))
    theta_0 = 0
    theta_1 = 0
    m = 4
    n = 1
    alpha = 0.1
    cost = 1000
    count = 0
    stop = 1
    while cost > 0.00000001 and count < stop:
        k0 = theta_0
        k1 = theta_1
        theta_0 = k0 - alpha*(1/m)*product_sum(k0, k1, 0)
        # theta_1 = k1 - alpha*(1/m)*product_sum(k0, k1, 1)
        for key in range(1,n+1):
            k = 0 if key == 0 else 1
            theta_1 = k0 - alpha*(1/m)*product_sum(k0, k1, k)

        cost = Cost_(theta_0, theta_1)
        count = count + 1
    return {'theta_0' : theta_0, 'theta_1': theta_1,
            'cost':cost, 'count':count}


for k,v in linear_regression().items():
    print(k,':', v)
TRAINING_SET = 0
