# # print "Hello Nicholas"
# print "Hi"
# x=7
# print x
#
# x=8
# y=10
# sum=x+y
# print sum
#
# x="Hello"
# y= "Good Evening"
# a=len(x)
# print x[a-1]
# print x[0:3]
# print x[-1]

# a=[7, 17, 4, 7, 11, 19, 45]
# b= ['red', 'blue']
#
# #print a, b
# #print a+b
# sum =0
# for n in a:
#     sum = sum + n
# print sum
#
# if (len(a)>len(b)):
#     print "a is longer"
#
# x=5
# y=10
#
# if(x==y):
#     print "HAPPY"
# else:
#     print "SAD"
#
# numberOfSevens=0
# for n in a:
#     if (n==7):
#         numberOfSevens = numberOfSevens + 1
# print numberOfSevens


# def sum(number):
#     initialSum = 0
#     for x in range(number+1):
#         initialSum = initialSum + x
#     return initialSum
#
# print sum(100)

def isPrime(number):
    for x in range(2, number, 1):
        if (number % x == 0):
            return False
    return True

def nextPrimeNumber(start):
    if (isPrime(start)):
        return start
    else:
        return nextPrimeNumber(start + 1)

print nextPrimeNumber(1000)