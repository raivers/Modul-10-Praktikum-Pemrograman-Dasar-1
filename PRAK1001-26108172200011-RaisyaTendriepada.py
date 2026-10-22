#test case 1
def factorial(n1):
    if n1 == 0:
        return 1
    return n1 * factorial(n1 - 1)

n1 = int(input())
print(str(n1) + "! = " + str(factorial(n1)))

#test case 2
def factorial(n2):
    if n2 == 0:
        return 1
    return n2 * factorial(n2 - 1)

n2 = int(input())
print(str(n2) + "! = " + str(factorial(n2)))

#test case 3
def factorial(n3):
    if n3 == 0:
        return 1
    return n3 * factorial(n3 - 1)

n3 = int(input())
print(str(n3) + "! = " + str(factorial(n3)))