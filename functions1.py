# ##Definition of a function
# def f(x):
#     return x*x
#
# print f(5)
#
# #count numberOfOccurenceOfElements
# def numberOfOccurenceOfElements(array,element):
#     numberOfOccurence=0
#     for n in array:
#         if (n==element):
#             numberOfOccurence = numberOfOccurence + 1
#     return numberOfOccurence
#
# print numberOfOccurenceOfElements([5, 'hi', 7, 8, 5, 5, 5, 5, 5], 5)
#
#function to print lyrics
# def repeat_lyrics():
#     print_lyrics() #Invoking a function2 in function 1
#     print_lyrics()
#
# def print_lyrics():
#     print "I'm a lumberjack, and I'm okay."
#     print "I sleep all night and I work all day."
# #
# repeat_lyrics()
# #
# # #function to print a string at 70th column
# def row():
#     def left_alignment():
#         print "Hi"
#         print_lyrics()
#     left_alignment()
#
# row()
#
# print ""
#
# def greet(s):
#     print "Hi " + s
# greet("Sri")
#
# def f(x):
#     y = x * x
#     return y
# print f(5)


# input: "Sri"
# output: "    Sri"
def justify(str, col):
    lengthOfString = len(str)
    numberOfBlanks = col - lengthOfString
    if lengthOfString < col:
        return numberOfBlanks * " " + str
    else:
        return str[lengthOfString-col:]

# test case
print justify("Sri", 7) == "    Sri"
print justify("Sri", 10) == "       Sri"
print justify("Sri", 1) == "i"
print justify("Sri", 2) == "ri"
print justify("Sri", 0) == ""

