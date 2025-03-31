#WAP to print the length of list

nums=["kunal","shruti","ajay","meena","tanu","sonu","monu"]
def P_length(nums):
    print(len(nums))
    return nums
P_length(nums)
#WAP to print the elements of list in a single line

def singel(nums):
    for i in nums:
        print(i,end=" ")
    return nums

singel(nums)



#WAP to find the factorial of n

n=int(input("\nenter the no.: "))
def cal_fact(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    print(fact)

cal_fact(n)

#WAP  to convert USD to INR

x=float(input("enter the $: "))
def convert(a):
    inr=x*85.56
    print("your INR is : ", inr)

convert(x)

#WAP to take input and check if no is odd print "ODD" if even print"EVEN

Z=int(input("enter the no: "))
def check(a):
    if a%2==0:
        print("EVEN")
    else:
        print("ODD")

check(Z)