#include <stdio.h>

int hanoi(int n) {
    if (n == 0) {
        return 0;
    }
    return 2 * hanoi(n - 1) + 1;
}

int main() {
    //test case 1
    int n1;
    scanf("%d", &n1);
    printf("The minimum number of steps for %d disks is %d\n", n1, hanoi(n1));

    //test case 2
     int n2;
    scanf("%d", &n2);
    printf("The minimum number of steps for %d disks is %d\n", n2, hanoi(n2));
    return 0;
}