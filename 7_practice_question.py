#write a recursive function to calculate the sum of first n natural numbers

n=int(input("enter the number: "))
def cal_sum(a):
    if a==0:
        return 0
    else:
        return cal_sum(a-1)+a
print(cal_sum(n))


#write recursive function to print all the elements in a list
# hint : use list and index as prameter

fruits=["apple","banana","mango","pineapple","grapes"]

def print_all(list1,idx=0):
    if idx==len(list1):
        return
    print(list1[idx])
    print_all(list1,idx+1)
print(print_all(fruits))