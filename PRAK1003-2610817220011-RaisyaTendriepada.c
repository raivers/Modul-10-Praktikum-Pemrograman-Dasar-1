#include <stdio.h>

int digit_sum(int n) {
    if (n < 10) {
        return n;
    }
    return n % 10 + digit_sum(n / 10);
}

int main() {
    //test case 1
    int n1;
    scanf("%d", &n1);
    printf("The sum of the digits of %d is %d\n", n1, digit_sum(n1));

    //test case 2
    int n2;
    scanf("%d", &n2);
    printf("The sum of the digits of %d is %d\n", n2, digit_sum(n2));
    return 0;
}