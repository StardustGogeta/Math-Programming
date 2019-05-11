#include <stdio.h>
#include <math.h>

void main() {
    unsigned long long n, d;
    printf("What is your number?\n");
    scanf("%llu", &n);
    printf("\n");
    if (n > 0) {
        for (d = 1; d <= sqrt(n); d++)
            if (n % d == 0)
                printf("%llu, %llu\n", n / d , d);
        printf("\nThe list of factor pairs has been successfully generated.\n");
    }
    else
        printf("\nInvalid number!\n");
}
