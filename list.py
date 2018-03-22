# HIGHER-ORDER FUNCTIONS

##Write a function called nested_sum that takes a nested list of integers and add up the elements
# from all of the nested lists.
#
# def nestedSum(l1):
#     sum = 0
#     for x in l1:
#         if isinstance(x, list):
#             sum += nestedSum(x)
#         else:
#             sum += x
#     return sum
#
# print nestedSum([[1], 1, [2, [7], 3]])
# print nestedSum([ 1, [1], 6])

# def sriMap(ls, f):
#     tempList = []
#     for x in ls :
#         # tempList += [f(x)]
#         tempList.append(f(x))
#     return tempList
#
# def square(x):
#     return x * x
# def cube(x):
#     return x * x * x
#
# print sriMap([1, 2, 3], square) # should return [1, 4, 9]
# print sriMap([1, 2, 3], cube) # should return [1, 8, 27]
#
# def sriFilter(ls, f):
#     tempList = []
#     for x in ls:
#         if f(x):
#             tempList.append(x)
#     return tempList
#
#
# # Test Cases
#
# def odd(x):
#     return x % 2 == 1
# def even(x):
#     return x % 2 == 0
# def big(x):
#     return x > 10
#
# print sriFilter([1,2,3,4,5], odd) # -> [1, 3, 5]
# print sriFilter([1,2,3,4,5], even) # -> [2, 4]
# print sriFilter([1,2,3,4,5], big) # -> []
# print sriFilter([0,5,10,15,20], big) # -> [15, 20]

## TODO: Learn REDUCE

# def cumulativefn1(ls):
#     output = []
#     sum =0
#     for x in ls:
#         sum += x
#         output.append(sum)
#     return output

# print cumulativefn1([[1], 1, [2, [7], 3]])
# print cumulativefn1([ 1, 1])
# print cumulativefn1([ 1, 2, 3])
#TODo: Another way of writing without using additional temp variable
# def cumulativefn1(ls):
#     output = [0]
#     for x in ls:
#         if isinstance(x, list):
#             output.append(output[-1] + x)
#     return output[1:]
#
# print cumulativefn1([1, 1])
# print cumulativefn1([1, 2, 3])
# print cumulativefn1([1, 2], 1)

##TODO: Function to sort a list in ascending or descending order

# def isSorted(ls):
#     original = ls[:]
#     for x in ls:
#         if isinstance(x, list):
#             isSorted(x)
#         else:
#             ls.sort()
#     return ls

# print isSorted([1, 3, 2])
# print isSorted([1, 3, 2, 4, 0])
# print isSorted([1, [3,1], 0])
# print isSorted([91, 18, 9, 99, [21, 3, 12, 9]])
# print isSorted(['b', 'a'])

# ##TODO: Return True if Element are ascending order else false
# def isSorted1(ls):
#     for i in range(len(ls)):
#         if ls[i + 1] == ls[i] or ls[i +1 ] > ls[i]:
#             return True
#         else:
#             return False
#
# print isSorted1([1, 3, 2])
# print isSorted1([1, 2, 1])
# print isSorted1([1, 2, 2])
# print isSorted1(['b', 'a'])

def isAnagram(str1, str2):
    ls1 = list(str1)
    ls1.sort()
    ls2 = list(str2)
    ls2.sort()
    print ls1, ls2
    return (ls1 == ls2)

print isAnagram('AB', 'BA')
print isAnagram("cat", "tac")
print isAnagram("hello", "lloeh")
print isAnagram("542", "254")







