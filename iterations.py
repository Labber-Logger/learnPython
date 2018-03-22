# #Execute exercise problems from Concept : Iterations

# def print_n(s, n):
#     if n <= 0:
#         return
#     print s
#     print_n(s, n-1)

# print "function output using while loop is below"
#
# def print_n(s, n):
#     while not (n <=0):
#         print s
#         n = n-1
#     else:
#         return
#
# print print_n(5, 4)

#FIND THE a POWER OF b

# def isPower(a, b):
#     n = 0
#     while True:
#         if b ** n == a:
#             return True
#         elif b ** n > a:
#             return False
#         n = n + 1
#
# print isPower(1, 4)
#
# def isPowerRecursive(a, b):
#     if a / b == 1:
#         return True
#     else:
#         return a % b == 0 and isPowerRecursive(a / b, b)
#
# print isPowerRecursive(125, 5)
# print isPowerRecursive(100, 5)

# Find GCD of a given number

# def gcdNumber(a, b):
#     if b == 0:
#         return a
#     elif not (a % b == 0):
#         return gcdNumber(b, a % b)
#     else:
#         return b
#
# print gcdNumber(54, 24) == 6
# print gcdNumber(24, 54) == 6
# print gcdNumber(42, 56) == 14
# print gcdNumber(4, 0) == 4
# print gcdNumber(0, 4) == 4
# print gcdNumber(4.0, 3)
# print gcdNumber(4.2, 24.8)

def eval_loop() :
    while True:
        input = raw_input( "Evaluation Input is : ")
        if input != "done" :
            print eval(input)

        else:
            previousValue = eval(input)
            return "Previous evaluated value is : ",previousValue

print eval_loop()

## Program for Infinite Series
# import math
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# def estimate_pi():
#     k = 0
#     sum = 0
#     constant = 2 * math.sqrt(2) / 9801
#
#     while True:
#         num = factorial(4 * k) * (1103 + 26390 * k)
#         den = factorial(k) **4 * 396 **(4*k)
#         fractionValue = constant * num /den
#         sum = sum + fractionValue
#         if abs(sum) < 1e-15:
#             break
#         k+1
#         return 1 / sum
#
# print estimate_pi()












