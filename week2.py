#Problem 1 - Write a function to find the longest common prefix string amongst an array of strings.
# def longestCommonPrefix(self, strs):
#     if not strs:
#         return ""
#     shortest = min(strs,key=len)
#     for i, ch in enumerate(shortest):
#         for other in strs:
#             if other[i] != ch:
#                 return shortest[:i]
#     return shortest
#
# print longestCommonPrefix()

#Problem 2 - reference - Learn Python, Chapter 5, Excercise 3
#Lesson learnt - Input validation check (Do it at the top of function)
# def check_fermat(a, b, c, n):
#     # a,b and c has to be positive and n greater than 2
#     if not(float(a).is_integer() and float(b).is_integer() and float(c).is_integer() and float(n).is_integer()):
#         return "Input is not an Integer"
#     if not(a > 0 and b > 0 and c > 0 and n > 2):
#         return "Input is not in the right range"
#     if ((a**n) + (b**n) == (c**n)):
#         return "Holy smokes, Fermat was wrong!"
#     else:
#         return "No, your input doesnt work"
#
# # print check_fermat(1, 1, 1.0, 3)
# # print check_fermat(1,0,1,3)
# # print check_fermat(1.5, 1.5, 1.5, 1)
# # print check_fermat(-1, -1, -1, 2)
# # print check_fermat(1, 1, 1, 3)
#
# a = input("Give me value for a: ")
# b = input("Give me value for b: ")
# c = input("Give me value for c: ")
# n = input("Give me value for n: ")
# print check_fermat(a, b, c, n)

# name = raw_input(" what is your name: ")
# print "Hello " + name

#problem 3-
# def traingleLargestSide(sidea, sideb, sidec):
#     if (sidea == sideb == sidec):
#         print "All sides are equal"
#     elif (sidea > sideb and sidea > sidec):
#         if (sideb > sidec):
#             print "Largest to least is " , sidea, sideb, sidec
#         else:
#             print "Largest to least is " , sidea, sidec, sideb
#     elif (sidea > sideb and sidea < sidec):
#         if (sideb > sidec):
#             print "Largest to least is " , sidea, sideb, sidec
#         else:
#             print "Largest to least is " , sidea, sidec, sideb
#
#traingleLargestSide( 4, 5, 4)

#problem4-
# def is_traingle(sidea,sideb,sidec):
#     #sides has to be positive real numbers
#     if not (float(sidea) > 0 and float(sideb) > 0 and float(sidec) > 0):
#         return "Input has to be real positive numbers"
#     if ((sidea > sideb + sidec) or (sideb > sidec + sidea) or (sidec > sidea + sideb)):
#         return "You can't create a triangle"
#     elif ((sidea == sideb + sidec) or (sideb == sidec + sidea) or (sidec ==sidea + sideb)):
#         return "This forms a degenrate triangle"
#     elif (sidea == sideb == sidec):
#         return "Equilateral triangle created"
#     else:
#         return "This is a traingle"
#
# print is_traingle(-1, -1.5, 2)
# print is_traingle(1, 1, 2)
# print is_traingle(2, 2, 1)
# print is_traingle('H', 'e', 'l')


# #problem5 - find distance between two points (x1, y1) and (x2, y2)
# import math
# def distanceCalculation(x1, y1, x2, y2):
#     dx = x2-x1
#     dy = y2-y1
#     dsquared = (dx**2) + (dy**2)
#     distance = math.sqrt(dsquared)
#     return distance

# print distanceCalculation(1,3,4,3)

#problem6- Finding hypotenuse of right traiangle
# import math
# def hypotenuse(sidea, sideb):
#     x = (sidea**2) + (sideb**2)
#     print "Value of sum of squares of each side" , x
#     hypo = math.sqrt(x)
#     return hypo
# print hypotenuse(3,4)

# def areaOfCircle(xc, yc, x1, y1):
#     radius = distanceCalculation(xc, yc, x1, y1)
#     area = math.pi * (radius ** 2)
#     return area
#
# print areaOfCircle(1,1,2,2)

# def is_between(x, y, z):
#     return x <= y <= z
#
# #print is_between(3, 3, 3)
#
# #testcase
# print is_between(3,3,3) == True
# print is_between(3,5,3) == True
# print is_between(3,0,0) == False

#PROBLEM 7 - FACTORIAL OF A NUMBER
# def factorial(n):
#     if (n == str):
#         return " Factorial is only defined for positive Integers"
#     if (n < 0):
#         return "Factorial is only defined for positive Integers"
#     elif (n==0):
#         return 1
#     else:
#         return n * factorial(n-1)
# print factorial("Hello")

#PROBLEM-8 FIBONNACCI SERIES TILL A NUMBER 'N'
# def fibonacci(n):
#     if (n ==0):
#         return 0
#     elif (n == 1):
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# print fibonacci(7)

# #PROBLEM 9 -
# def akermannFunction(m, n):
#     if not (m >= 0 and n >= 0):
#         print "Function is only defined for non-negetive integers of m and n"
#         return None
#     elif (m == 0):
#         return n + 1
#     elif (n == 0):
#         return akermannFunction(m - 1, 1)
#     else:
#         # temp3 = akermannTheory(m, n-1)
#         # temp4 = akermannTheory(m-1, temp3)
#         # return temp4
#         return akermannFunction(m - 1, akermannFunction(m, n - 1))
#
# print akermannFunction(1, 1) == 3
# print akermannFunction(3, 4) == 125
# print akermannFunction(1, 4) == 6
# print akermannFunction(0, 0) == 2
# print akermannFunction(4, 4)

#PROBLEM -10
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]
#
# def isPalindrome(word):
#     if first(word) == last(word):
#         stringLength = len(middle(word))
#         for n in range(stringLength):
#             return isPalindrome(middle(word))
#         return True
#
#     else:
#            return False
#            print "string is not a palindrome"

def isPalindrome(word):
    if len(word) <= 1:
        return True
    elif first(word) != last(word):
        return False
    else:
        return isPalindrome(middle(word))

while (True):
    word = raw_input("Word: ")
    print isPalindrome(word)

# print middle("LeveL")
# print middle("redivider")
# print middle("AA")
# print middle("A")
# print middle(' ')
# print isPalindrome("read")
# print isPalindrome("level")
# print isPalindrome("redder")
# print isPalindrome("redeader")
# print isPalindrome("redeaaeder")











