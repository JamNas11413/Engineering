# logarithm
import math

print(f"Logarithm base 2 of 16 is: {math.log(16, 2)}")

# factorial
def calc_factorial(n):
    factorial = 1
    for i in range(2, n+1):
        factorial *= n
    return factorial
print(calc_factorial(5))


first_num = calc_factorial(3)  # 9
sec_num = calc_factorial(4)  # 64

print(first_num)
print(sec_num)
print(sec_num - first_num)  # 55
