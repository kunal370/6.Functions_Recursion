a=5
b=6
sum=a+b
print(sum)

#more lines of code
a=10
b=10
sum=a+b
print(sum)

a=11
b=11
sum=a+b
print(sum)

print("*****************************************")

#redundant code==> repeating same line of code


def add(a,b):
    sum=a+b
    print(sum)
    return sum

add(5,6)

add(10,10)

add(11,11)
print("*****************************************")

#fuction defination
def cal_sum(x,y): # parameters
    return x+y


sum=cal_sum(2,5) # function call; arguments
print(sum)


print("*****************************************")

def print_hello():
    print("helloww")

print_hello()
print_hello()

print(print_hello())
'''
function which does not return anything always give none as output'''


