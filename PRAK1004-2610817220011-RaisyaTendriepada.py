#test case 1
def hanoi(n1):
    if n1 == 0:
        return 0
    return 2 * hanoi(n1 - 1) + 1

n1 = int(input())
print("The minimum number of steps for " + str(n1) + " disks is " + str(hanoi(n1)))

#test case 1
def hanoi(n2):
    if n2 == 0:
        return 0
    return 2 * hanoi(n2 - 1) + 1

n2 = int(input())
print("The minimum number of steps for " + str(n2) + " disks is " + str(hanoi(n2)))