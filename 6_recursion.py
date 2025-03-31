
n=int(input("enter the number: "))
def show(a):
    if(a==0): # this is base case
        return
    print(a)
    show(a-1)
#function calling itself "recursive function"
show(n)

#factorial of number using recursion

def cal_fact(a):
    if a==1 or a==0:
        return 1
    else:
        return cal_fact(a-1)*a

print(cal_fact(n))

