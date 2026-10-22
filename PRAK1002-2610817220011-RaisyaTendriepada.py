#test case 1
def fibonacci(n1):
    if n1 == 0:
        return 0
    if n1 == 1:
        return 1
    return fibonacci(n1 - 1) + fibonacci(n1 - 2)

n1 = int(input())
for i in range(n1):
    print(fibonacci(i), end=" ")
print()

#test case 2
def fibonacci(n2):
    if n2 == 0:
        return 0
    if n2 == 1:
        return 1
    return fibonacci(n2 - 1) + fibonacci(n2 - 2)

n2 = int(input())
for i in range(n2):
    print(fibonacci(i), end=" ")
print()