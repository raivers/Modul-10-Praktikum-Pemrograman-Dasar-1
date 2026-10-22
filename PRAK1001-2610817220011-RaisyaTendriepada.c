#include <stdio.h>

int factorial(int n) {
    if (n == 0) {
        return 1;
    }
    return n * factorial(n - 1);
}

int main() {
    //test case 1
    int n1;
    scanf("%d", &n1);
    printf("%d! = %d\n", n1, factorial(n1));

    //test case 2
    int n2;
    scanf("%d", &n2);
    printf("%d! = %d\n", n2, factorial(n2));

    //test case 3
    int n3;
    scanf("%d", &n3);
    printf("%d! = %d\n", n3, factorial(n3));
    return 0;
}