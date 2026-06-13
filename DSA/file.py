# # logarithm
# import math

# print(f"Logarithm base 2 of 16 is: {math.log(16, 2)}")

# # factorial
# def calc_factorial(n):
#     factorial = 1
#     for i in range(2, n+1):
#         factorial *= n
#     return factorial
# print(calc_factorial(5))


# first_num = calc_factorial(3)  # 9
# sec_num = calc_factorial(4)  # 64

# print(first_num)
# print(sec_num)
# print(sec_num - first_num)  # 55



# find the min
def min(lst: list[int]) -> int:
    min = lst[0] # lets the 1st num be min
    if len(lst) == 0:
        return None   # when a return statement excuted the remaining statemnets are not exe in a func 
    for i in lst:
        if min > i:
            min  = i
    return min
print(min([5,6,6,1,2,3,4]))  # 1 


# reversing a str
def reverse_str(str):
    reverse_str = ''
    for i in reversed(str):
        reverse_str += i
    return reverse_str

print(reverse_str('jamal kamal khan'))