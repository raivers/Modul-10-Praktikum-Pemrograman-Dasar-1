#include <stdio.h>

int fibonacci(int n) {
    if (n == 0) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    //test case 1
    int n1;
    scanf("%d", &n1);
    for (int i = 0; i < n1; i++) {
        printf("%d ", fibonacci(i));
    }
    printf("\n");

    //test case 2
     int n2;
    scanf("%d", &n2);
    for (int i = 0; i < n2; i++) {
        printf("%d ", fibonacci(i));
    }
    printf("\n");
    return 0;
}