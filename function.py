
def calc_avg(a,b,c):
    ans = (a+b+c)/3
    return ans

print(calc_avg(2,3,4))

#default parameter
def cal_prod(a,b=2):
    print(a*b)
    return a*b

cal_prod(1)

cities=["delhi","sylhet","dhaka","kolkata"]
heroes=["saktimaan","captain america","krish"]

def print_len(list):
    print(len(list))

print_len(cities)
print(len(heroes))

def print_list(list):
    for item in list:
       print(item,end=" ")

print_list(heroes)

#factorial
def calc_func(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
print("\n")
calc_func(5)

#recursion
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)