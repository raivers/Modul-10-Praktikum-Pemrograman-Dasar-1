#test case 1
def digit_sum(n1):
    if n1 < 10:
        return n1
    return n1 % 10 + digit_sum(n1 // 10)

n1 = int(input())
print("The sum of the digits of " + str(n1) + " is " + str(digit_sum(n1)))

#test case 2
def digit_sum(n2):
    if n2 < 10:
        return n2
    return n2 % 10 + digit_sum(n2 // 10)

n2 = int(input())
print("The sum of the digits of " + str(n2) + " is " + str(digit_sum(n2)))