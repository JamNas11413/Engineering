# functions



# PRACTICE
# WAF TO PRINT THE ELEMENT OF A LIST IN A SINGLE LINE
lst=[1,2,3,4,5,6,7,8,9]
def sam_line(list):
    for item in list:
        print(item, end=" ")

sam_line(lst)

# wa func to convert usd to pkr
def usd_pkr(usd):
    pkr=usd*100
    print("PKR =",pkr)
    return pkr
s=usd_pkr(150)
print(s)






import numbers


# RECURSION
    # WHEN A FUNC CALL ITSELF REPEATEDLY.
    # SAME WORK CAN DO BY RECURSIO AND LOOPS, JUST DEPEND ON CASE WHERE WHICH ONE WILL MORE APPROPRIATE
    #
    #
def show(n):
    print(n)
show(5) # 5

# if i wanna print 5-1
def show(n):
    if n==0:        # base case(kaha tak chala ga)
        return      # if i don't enter any value then it means that i wanna controle return
    print(n)
    show(n-1)
    print("End")
show(5)

# if i remove the base line it will become infinite, and ultimately will full memory and our code crash

n=0
sum=0
while n<=100:
    sum=sum+n
    n=n+1
print(sum)



## PRACTICE

# wa recursion to calc sum of 1st n np.
def sum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
sum(100)

def calc_sum(n):
    if n == 0:
        return 0
    print(n)
    calc_sum(n-1)
calc_sum(5)
now in rec


# @. WRITE A RECURSIVE FUNC TO PRINT ALL ELEMENT IN A LIST.hint USE LIST AND INDEX AS PERAMETER
def all_ele(list,idx=0):
    if idx == len(list):
        return
    print(list[idx])
    return all_ele(list,idx+1)
lst=["jamal","ijaz","ilyas","Maryam BiBi"]
print(all_ele(lst))

def show(n):
    if n >= 11:
        return
    print(n)
    show(n+1)
show(5)

# import sys
# get.recursion()


friends=("jamal","ijaz","Maryam","ilyas")
def ele_lst(list,idx=0):
    if idx==len(list):
        return
    print(list[idx])
    idx+=1
    return ele_lst(list,idx)
ele_lst(friends)

inp=int(input("Enter a number: "))
x=0
def table(n):
    global x
    x+=1
    if x==17:
        return
    print(f"{n}*{x}={n*x}")
    return table(n)
table(inp)

